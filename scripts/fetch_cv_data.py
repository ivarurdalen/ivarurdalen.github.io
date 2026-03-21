"""Fetch CV data from Google Sheets and save as local CSV."""

from pathlib import Path

import pandas as pd

SHEET_ID = "1mORzRlwt7in5yxdu7UiMhEDQQJQWvuXeqcFjh_dP0Qo"
GID = "1914763824"
CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"
)
OUTPUT_PATH = Path("data/cv_data.csv")


def main():
    df = pd.read_csv(CSV_URL)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
