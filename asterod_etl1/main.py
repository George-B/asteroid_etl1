from extract import fetch_asteroids
from transform import transform_data
from load import load_data
from datetime import datetime, timedelta
from config import DB_CONFIG
print("DB CONFIG:", DB_CONFIG)

def run_pipeline():
    start_date = datetime.today()
    end_date = start_date + timedelta(days=3)  # 👈 fetch multiple days

    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")

    raw_data = fetch_asteroids(start_str, end_str)
    print("RAW DATA KEYS:", raw_data.keys() if raw_data else None)

    if raw_data:
        transformed = transform_data(raw_data)
        print("TRANSFORMED COUNT:", len(transformed))
        print("TRANSFORMED SAMPLE:", transformed[:2])  # 👈 preview

        if transformed:
            print("LOADING DATA...")
            load_data(transformed)
        else:
            print("⚠️ No transformed data (check transform.py)")
    else:
        print("❌ No raw data from API")

if __name__ == "__main__":
    run_pipeline()

