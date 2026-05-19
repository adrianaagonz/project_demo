from pathlib import Path

# This finds the main folder "project_demo" automatically
ROOT = Path(__file__).resolve().parent.parent

# Change these paths to point to your data files
RAW_PATH = ROOT / "data" / "raw" / "sephora_products.csv"
OUT_PATH = ROOT / "data" / "processed" / "clean_dataset.csv"