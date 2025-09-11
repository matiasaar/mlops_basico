import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os
from google.cloud import storage

# --- Carga del Modelo ---
# Descargar el modelo desde GCS si no existe localmente
if not os.path.exists('model.joblib'):
    storage_client = storage.Client()
    bucket_name = os.environ.get("GCS_BUCKET")  # evita error si no existe
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob("models/taxi-fare-predictor/model.joblib")
    blob.download_to_filename("model.joblib")

model = joblib.load("model.joblib")

# --- Definición de la App y los Datos de Entrada ---
app = FastAPI(title="API de Predicción de Tarifas de Taxi")

# Clase con los atributos de entrada
class TaxiFeatures(BaseModel):
    pickup_location_id: int
    dropoff_location_id: int
    passenger_count: int
    # No incluimos fare_amount, ya que es lo que vamos a predecir

@app.post("/predict")
def predict(features: TaxiFeatures):
    # Convertir los datos de entrada a un DataFrame
    df = pd.DataFrame([features.dict()])

    # Realizar la predicción
    prediction = model.predict(df)[0]

    return {"predicted_fare": prediction}