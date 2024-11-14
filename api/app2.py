from pydantic import BaseModel, Field
from typing import Literal
from fastapi import FastAPI, HTTPException
import json
from catboost import CatBoostRegressor
import joblib

app2 = FastAPI()

class InputData(BaseModel):
    Number_of_bedrooms: int = Field(..., ge=2, le=5)  # 
    Living_area: int = Field(..., ge=50, le=300)  
    Open_fire: bool
    Swimming_Pool: bool
    Kitchen_type: Literal["Installed", "Hyper equipped", "Semi equipped", "Not installed"]
    Number_of_facades: int = Field(..., ge=1, le=5)
    State_of_building: Literal["As new", "Good", "Just renovated", "To be done up", "To renovate"]
    epc: Literal["A", "B", "C", "D", "E", "F"]
    landSurface: int = Field(..., ge=100, le=1200)  
    Province: Literal["Brussels", "Antwerp", "Brabant_Wallon", "Flemish Brabant", "Liège", "Namur", 
                      "Luxembourg", "Hainaut", "West Flanders", "East Flanders", "Limburg"]    
  
@app2.get("/") 
async def read_root(): 
    return "still alive for PR" 

# Define the /predict endpoint
@app2.post("/predict")
async def predict(input: InputData):
    try:     
        dict_input = input.model_dump()
        input_list = list(dict_input.values())
        poilynomia_features_model = joblib.load(r'C:\repos\immo-eliza-ml\poilynomia_features_model')
        themodel = joblib.load(r'C:\repos\immo-eliza-ml\themodel')
        prediction = model.predict(input_list)
        return {"prediction": prediction}

    except Exception as e:
        # Handle errors (e.g., missing input or invalid format)
        raise HTTPException(status_code=400, detail=str(e))
    
### uvicorn api.app2:app2 in bash



# load and predict
X_val_prep = poilynomia_features_model.transform(X_test)
predictions = themodel.predict(X_val_prep)


print("RMSE on test data is: ", root_mean_squared_error(y_test, predictions))

r2 = r2_score(y_test, predictions)
print("R2 Score with real prices:", r2)
