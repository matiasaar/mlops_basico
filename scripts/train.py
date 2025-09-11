import pandas as pd
from google.cloud import bigquery
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from google.cloud import storage

# --- 1. Carga de Datos desde BigQuery ---
PROJECT_ID = "mlopsbasico"
DATASET = "taxi_data"
TABLE = "taxi_fares_cleaned"

client = bigquery.Client(project=PROJECT_ID)
query = f"SELECT * FROM `{PROJECT_ID}.{DATASET}.{TABLE}`"
df = client.query(query).to_dataframe()

# --- 2. Preparación de Datos y Entrenamiento del Modelo ---
X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo simple para demostración
model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# --- 3. Evaluación del Modelo ---
preds = model.predict(X_test)
rmse = mean_squared_error(y_test, preds )  # squared=False devuelve RMSE directamente
print(f"RMSE del modelo en el set de prueba: {rmse:.2f}")

# --- 4. Guardar el Artefacto del Modelo ---
joblib.dump(model, "model.joblib")

# --- 5. Subir el artefacto a Cloud Storage ---
BUCKET_NAME = "mlopsbucket12"  # cámbialo por tu bucket real
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

blob = bucket.blob("model.joblib")
blob.upload_from_filename("model.joblib")

print("Modelo subido a Cloud Storage correctamente ✅")
