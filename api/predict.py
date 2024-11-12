import json
from catboost import CatBoostRegressor

# Load the model
model = CatBoostRegressor()
model = model.load_model(r"C:\repos\immo-eliza-ml\CB_model", format='cbm')

# Function to read JSON input file, make prediction, and output JSON
def make_prediction(input_json_path, output_json_path):
    with open(input_json_path, 'r') as input_file:
        dict_input = json.load(input_file) 
        input_list = list(dict_input.values())
        prediction = model.predict(input_list)
    with open(output_json_path, 'w') as output_file:
        json.dump(prediction,output_file)    

