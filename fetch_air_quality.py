import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from google.cloud import bigquery

# 1. Load Environment Variables
load_dotenv()

# API Keys and Security
API_KEY = os.getenv("OPENWEATHER_API_KEY")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-key.json"

# Cloud Configuration (Pulled from .env or defined here)
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET_ID = os.getenv("GCP_DATASET_ID")
TABLE_ID = os.getenv("GCP_TABLE_ID")

# Create the full path safely
if all([PROJECT_ID, DATASET_ID, TABLE_ID]):
    TABLE_FULL_PATH = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
else:
    raise ValueError("Missing GCP configuration in .env file")

# 2. Targeted Cities (The Original Four)
CITIES = {
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Birmingham": {"lat": 52.4862, "lon": -1.8904},
    "Glasgow": {"lat": 55.8642, "lon": -4.2518},
    "Manchester": {"lat": 53.4808, "lon": -2.2426}
}

def fetch_aqi_data():
    """Fetches air quality data from OpenWeather API and returns a DataFrame."""
    all_data = []
    print(f"--- Fetching data for {len(CITIES)} cities ---")
    
    for city, coords in CITIES.items():
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={coords['lat']}&lon={coords['lon']}&appid={API_KEY}"
        try:
            response = requests.get(url).json()
            
            data = {
                "city": city,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "aqi": response['list'][0]['main']['aqi'],
                "no2": response['list'][0]['components']['no2'],
                "pm2_5": response['list'][0]['components']['pm2_5']
            }
            all_data.append(data)
            print(f"Successfully fetched data for {city}")
        except Exception as e:
            print(f"Failed to fetch data for {city}: {e}")
            
    return pd.DataFrame(all_data)

def upload_to_bigquery(df):
    """Streams the DataFrame into the BigQuery table."""
    try:
        client = bigquery.Client()
        print(f"Connecting to BigQuery: {TABLE_FULL_PATH}...")
        
        # load_table_from_dataframe uses 'pyarrow' under the hood
        job = client.load_table_from_dataframe(df, TABLE_FULL_PATH)
        job.result()  # Wait for the upload to complete
        
        print(f"✅ SUCCESS: Uploaded {len(df)} rows to BigQuery.")
    except Exception as e:
        print(f"❌ ERROR: Cloud upload failed. Reason: {e}")

if __name__ == "__main__":
    # Execute the Pipeline
    df_air_quality = fetch_aqi_data()
    
    print("\n--- Local Data Preview ---")
    print(df_air_quality)
    print("--------------------------\n")
    
    if not df_air_quality.empty:
        upload_to_bigquery(df_air_quality)
    else:
        print("No data collected. Skipping upload.")
