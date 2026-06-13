import pandas as pd

def create_silver_fred(df: pd.DataFrame) -> pd.DataFrame:
    silver = df.copy()
    
    silver = silver.rename(
        columns={
            "date": "observation_date",
            "value": "indicator_value"
        }
    )
    
    silver["observation_date"] = pd.to_datetime(
        silver["observation_date"],
        errors="coerce"
    )
    
    silver["indicator_value"] = pd.to_numeric(
        silver["indicator_value"],
        errors="coerce"
    )
    
    silver = silver.dropna(
        subset=["series_id", "observation_date", "indicator_value"]
    )
    
    silver = silver.drop_duplicates(
        subset=["series_id", "observation_date"]
    )
    
    return silver