from pathlib import Path


def load_csv(path: str | Path):
    """Load a CSV file into a DataFrame."""
    import pandas as pd
    return pd.read_csv(path)

def load_sephora_data():
    """Find the Sephora dataset automatically in data/raw using Path and load it using the load_csv function.."""
    # project_root goes up two levels (from src.io.py to project_demo)
    project_root = Path(__file__).resolve().parents[1]
    
    # Construct relative path to data/raw/sephora_products.csv
    file_path = project_root / "data" / "raw" / "sephora_products.csv"
    
    print(f"loading data from: {file_path}")
    return load_csv(file_path)