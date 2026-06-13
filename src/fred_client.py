import requests
import pandas as pd

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"


# Getting FRED series data as dataframe
def get_series(series_id, api_key):
    
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json"
    }
    
    response = requests.get(
        BASE_URL,
        params=params,
        timeout=30
    )
    
    response.raise_for_status()
    
    df = pd.DataFrame(
        response.json()["observations"]
    )
    
    df["series_id"] = series_id
    
    return df