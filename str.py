import streamlit as st
import requests
from pydantic import BaseModel, Field
from typing import Literal

# Define input structure
class InputData(BaseModel):
    Number_of_bedrooms: int = Field(..., ge=2, le=5)
    Living_area: int = Field(..., ge=50, le=300)
    Open_fire: bool
    Swimming_Pool: bool
    Kitchen_type: Literal["Installed", "Hyper equipped", "Semi equipped", "Not installed"]
    Number_of_facades: int = Field(..., ge=1, le=5)
    State_of_building: Literal["As new", "Good", "Just renovated", "To be done up", "To renovate"]
    epc: Literal["A", "B", "C", "D", "E", "F"]
    landSurface: int = Field(..., ge=100, le=1200)
    Province: Literal[
        "Brussels", "Antwerp", "Brabant_Wallon", "Flemish Brabant", "Liège", "Namur",
        "Luxembourg", "Hainaut", "West Flanders", "East Flanders", "Limburg"
    ]

# Streamlit App
def main():
    st.title("Real Estate Price Prediction")

    # Collect user inputs
    Number_of_bedrooms = st.number_input("Number of Bedrooms", min_value=2, max_value=5, step=1)
    Living_area = st.number_input("Living Area (m²)", min_value=50, max_value=300, step=1)
    Open_fire = st.checkbox("Open Fire")
    Swimming_Pool = st.checkbox("Swimming Pool")
    Kitchen_type = st.selectbox("Kitchen Type", ["Installed", "Hyper equipped", "Semi equipped", "Not installed"])
    Number_of_facades = st.number_input("Number of Facades", min_value=1, max_value=5, step=1)
    State_of_building = st.selectbox("State of Building", ["As new", "Good", "Just renovated", "To be done up", "To renovate"])
    epc = st.selectbox("EPC Rating", ["A", "B", "C", "D", "E", "F"])
    landSurface = st.number_input("Land Surface (m²)", min_value=100, max_value=1200, step=1)
    Province = st.selectbox("Province", [
        "Brussels", "Antwerp", "Brabant_Wallon", "Flemish Brabant", "Liège", "Namur",
        "Luxembourg", "Hainaut", "West Flanders", "East Flanders", "Limburg"
    ])

    # Button to submit for prediction
    if st.button("Get Prediction"):
        # Create an instance of InputData with the user's inputs
        input_data = InputData(
            Number_of_bedrooms=Number_of_bedrooms,
            Living_area=Living_area,
            Open_fire=Open_fire,
            Swimming_Pool=Swimming_Pool,
            Kitchen_type=Kitchen_type,
            Number_of_facades=Number_of_facades,
            State_of_building=State_of_building,
            epc=epc,
            landSurface=landSurface,
            Province=Province
        )

        # Send request to FastAPI backend
        try:
            response = requests.post("http://127.0.0.1:8000/predict", json=input_data.dict())
            if response.status_code == 200:
                prediction = response.json().get("prediction")
                st.success(f"Predicted Price: € {prediction}")
            else:
                st.error(f"Error: {response.json().get('detail')}")
        except requests.exceptions.RequestException as e:
            st.error("Error connecting to the prediction API. Make sure FastAPI is running.")

if __name__ == "__main__":
    main()
