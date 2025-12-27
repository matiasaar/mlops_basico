import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

def train(data_dir: str, model_dir: str):
    X_train = pd.read_csv(f"{data_dir}/X_train.csv")
    y_train = pd.read_csv(f"{data_dir}/y_train.csv").values.ravel()

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    joblib.dump(model, f"{model_dir}/model.joblib")
    print("✅ Model trained")

if __name__ == "__main__":
    train("data/processed", "model")
