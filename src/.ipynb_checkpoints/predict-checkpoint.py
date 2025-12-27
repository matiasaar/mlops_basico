import joblib
import pandas as pd

model = joblib.load("model/model.joblib")
scaler = joblib.load("data/processed/scaler.joblib")
columns = joblib.load("data/processed/columns.joblib")

def predict(instance: dict):
    df = pd.DataFrame([instance])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    X = scaler.transform(df)
    prob = model.predict_proba(X)[0][1]

    return {"churn_probability": float(prob)}
