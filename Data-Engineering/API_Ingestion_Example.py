
import requests
import pandas as pd
from pathlib import Path

API_URL = "https://placeholder.publicAPI.com/posts"
OUTPUT_DIR = Path("data_engineering_output")
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "posts.csv"

def fetch_data():
    resp = requests.get(API_URL, timeout=10)
    resp.raise_for_status()
    return resp.json()

def to_dataframe(records):
    return pd.DataFrame(records)

def save_to_csv(df: pd.DataFrame, path: Path):
    df.to_csv(path, index=False)
    print(f"Saved {len(df)} records to {path}")

if __name__ == "__main__":
    records = fetch_data()
    df = to_dataframe(records)
    save_to_csv(df, OUTPUT_FILE)
