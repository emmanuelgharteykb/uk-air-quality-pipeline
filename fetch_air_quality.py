import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from google.cloud import bigquery

# 1. Load Environment Variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-key.json"

# 2. Configuration - Cleaned up strings
CITIES = {
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Birmingham": {"lat": 52.4862, "lon": -1.8904},
    "Glasgow": {"lat": 55.8642, "lon": -4.2518},
    "Manchester": {"lat": 53.4808, "lon": -2.2426}
}

PROJECT_ID = "uk-air-quality-pipeline"
DATASET_ID = "air_quality_data"
TABLE_ID = "uk_aqi_logs"
TABLE_FULL_PATH = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

def fetch_aqi_data():
    all_data = []
    for city, coords in CITIES.items():
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={coords['lat']}&lon={coords['lon']}&appid={API_KEY}"
        response = requests.get(url).json()
        
        data = {
            "city": city,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "aqi": response['list'][0]['main']['aqi'],
            "no2": response['list'][0]['components']['no2'],
            "pm2_5": response['list'][0]['components']['pm2_5']
        }
        all_data.append(data)
    return pd.DataFrame(all_data)

def upload_to_bigquery(df):
    try:
        client = bigquery.Client()
        print(f"Connecting to BigQuery project: {PROJECT_ID}...")
        
        job = client.load_table_from_dataframe(df, TABLE_FULL_PATH)
        job.result()  # Wait for completion
        print(f"✅ SUCCESS: Uploaded {len(df)} rows to {TABLE_FULL_PATH}")
    except Exception as e:
        print(f"❌ ERROR: Could not upload to BigQuery. Reason: {e}")

if __name__ == "__main__":
    df_air_quality = fetch_aqi_data()
    print("--- Local Data Preview ---")
    print(df_air_quality)
    print("--------------------------")
    upload_to_bigquery(df_air_quality)
