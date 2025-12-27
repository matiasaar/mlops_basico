import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess(input_path: str, output_dir: str):
    df = pd.read_csv(input_path)

    # Target encoding
    df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # One-hot encoding
    X = pd.get_dummies(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save artifacts
    joblib.dump(scaler, f"{output_dir}/scaler.joblib")
    joblib.dump(X_train.columns, f"{output_dir}/columns.joblib")

    pd.DataFrame(X_train_scaled).to_csv(f"{output_dir}/X_train.csv", index=False)
    pd.DataFrame(X_test_scaled).to_csv(f"{output_dir}/X_test.csv", index=False)
    y_train.to_csv(f"{output_dir}/y_train.csv", index=False)
    y_test.to_csv(f"{output_dir}/y_test.csv", index=False)

    print("✅ Preprocessing completed")

if __name__ == "__main__":
    preprocess("data/raw/telco.csv", "data/processed")
