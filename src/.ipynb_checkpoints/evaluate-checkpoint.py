import pandas as pd
import joblib
from sklearn.metrics import roc_auc_score

def evaluate(data_dir: str, model_dir: str):
    X_test = pd.read_csv(f"{data_dir}/X_test.csv")
    y_test = pd.read_csv(f"{data_dir}/y_test.csv").values.ravel()

    model = joblib.load(f"{model_dir}/model.joblib")

    probs = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, probs)

    print(f"AUC: {auc:.3f}")

    if auc < 0.75:
        raise ValueError("  Model rejected")

    print(" Model approved")

if __name__ == "__main__":
    evaluate("data/processed", "model")
