import pandas as pd

def clean(df: pd.DataFrame) -> pd.DataFrame:
    """ Clean the sephora dataset by handling missing values and removing duplicates."""
    df_clean = df.copy()

    # 1. Fill missing sale prices.
    df_clean['sale_price_usd'] = df_clean['sale_price_usd'].fillna(df_clean['price_usd'])

    # 2. Fill missing ingredients.
    df_clean['ingredients'] = df_clean['ingredients'].fillna('Not Scpecified')

    # 3. Drop duplicate rows.
    df_clean = df_clean.drop_duplicates()

    print("Data cleaning completed successfully!")
    return df_clean
