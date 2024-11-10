from fastapi import FastAPI
from pydantic import BaseModel, Field, conint, constr
from typing import Literal

app = FastAPI()

class House(BaseModel):
    Number_of_bedrooms: conint(ge=2, le=5) #2 to 5
    Living_area: conint(ge=50, le=300)  #50 to 300
    Open_fire: bool
    Swimming_Pool: bool
    Kitchen_type:Literal ["Installed","Hyper equipped","Semi equipped","Not installed "]
    Number_of_facades: int
    State_of_building:Literal ["As new","Good","Just renovated","To be done up","To renovate"]
    epc: Literal["A","B","C","D","E","F"]
    landSurface: int ## 0 to 1200,
    Province:Literal ["Brussels","Antwerp","Brabant_Wallon","Flemish Brabant","Liège","Namur","Luxembourg","Hainaut","West Flanders","East Flanders","Limburg"]




@app.get("/house/{itemid}")
async def create_house(house: House):
    return house

#C:\repos\immo-eliza-deployment> fastapi dev api\app.py   =>  Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     127.0.0.1:60613 - "GET /items/foo HTTP/1.1" 422 Unprocessable Entity
# INFO:     127.0.0.1:60614 - "GET /items/8 HTTP/1.1" 200 OK

