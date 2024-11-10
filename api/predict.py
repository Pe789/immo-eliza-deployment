from catboost import CatBoostRegressor
model = CatBoostRegressor()
model = model.load_model(r"C:\repos\immo-eliza-ml\CB_model", format='cbm')
data = [3, 150, False, False, "Installed", 3, "Good", "A", 450, "Brussels" ]


prediction = model.predict(data,
        prediction_type=None,
        ntree_start=0,
        ntree_end=0,
        thread_count=-1,
        verbose=None,
        task_type="CPU")

print(prediction) 