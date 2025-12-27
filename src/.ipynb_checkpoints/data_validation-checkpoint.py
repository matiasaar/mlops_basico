import pandas as pd

def validate_data(path: str):
    df = pd.read_csv(path)

    expected_columns = [
        "tenure", "MonthlyCharges", "Contract", "Churn"
    ]

    # Check columns
    for col in expected_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    # Check values
    if df["tenure"].min() < 0:
        raise ValueError("Tenure has negative values")

    if not df["Churn"].isin(["Yes", "No"]).all():
        raise ValueError("Invalid churn values")

    print("✅ Data validation passed")

if __name__ == "__main__":
    validate_data("data/raw/telco.csv")
