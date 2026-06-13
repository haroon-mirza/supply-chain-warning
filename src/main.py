import pandas as pd

from fred_client import get_series
from postgres_loader import load_dataframe
from config import FRED_API_KEY

SERIES_IDS = [
    "IPMAN",
    "RSAFS",
    "UNRATE",
    "INDPRO",
    "ISRATIO",
    "HOUST",
    "TSR"
]


# Main function to select data
def main():
    
    print("starting pipeline")
    
    all_dfs = []
    
    for series in SERIES_IDS:
        try:
            print(f"Getting {series}")
            df = get_series(series, FRED_API_KEY)
            all_dfs.append(df)
            
        except Exception as e:
            print(f"Failed to load {series}: {e}"
            )
    
    combined_df = pd.concat(
        all_dfs,
        ignore_index=True
    )
    
    load_dataframe(
        combined_df,
        "fred_data"
    )
    
    print(
        f"Loaded {len(combined_df)} rows"
    )
    
if __name__ == "__main__":
    main()