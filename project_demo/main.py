from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns
from src.viz import plot_graph


def main():
    """ Main pipeline to execute the reproducible EDA for sephora products."""
    # 1. Load the raw data using the path from config.py
    df = load_csv(RAW_PATH)

    # 2. Clean missing values and remove duplicates.
    df = clean(df)

    # 3. Passthrough features function from the template.
    df = build_features(df)

    # 4. Column validation (kept commented as in the original template).
    # assert_columns(df, ['column_1', 'column_2'])

    # 5. Generate and save the exploratory plots.
    plot_graph(df)

    # 6. Create the processed data directory and save the clean dataset.

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")

if __name__ == "__main__":
    main()
