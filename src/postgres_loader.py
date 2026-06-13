from sqlalchemy import create_engine

from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

def get_engine():
    
    conn_string = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    
    return create_engine(conn_string)

def load_dataframe(
    df,
    table_name
):


    engine = get_engine()
    
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )