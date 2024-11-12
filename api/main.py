

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import Union

app = FastAPI()

class Input(BaseModel):
    salary: float
    bonus: float
    taxes: float


@app.post("/calculate/")
async def calculate_salary(input: Input) -> dict:
    # Perform the salary calculation
    net_income = input.salary + input.bonus - input.taxes
    try:
        return {"result": net_income}

    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
   
## in git : uvicorn api.main:app