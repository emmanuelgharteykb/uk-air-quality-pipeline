import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# 2. Configuration - Cities & Coordinates
CITIES = {
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Birmingham": {"lat": 52.4862, "lon": -1.8904},
    "Glasgow": {"lat": 55.8642, "lon": -4.2518},
    "Manchester": {"lat": 53.4808, "lon": -2.2426}
}

def fetch_air_quality():
    """Fetches real-time AQI data and returns a cleaned DataFrame."""
    if not API_KEY:
        print("❌ Error: No API Key found. Check your .env file.")
        return None

    results = []
    
    for city, coords in CITIES.items():
        url = (
            f"http://api.openweathermap.org/data/2.5/air_pollution?"
            f"lat={coords['lat']}&lon={coords['lon']}&appid={API_KEY}"
        )
        
        try:
            response = requests.get(url)
            response.raise_for_status() # Check for HTTP errors
            
            data = response.json()['list'][0]
            components = data['components']
            
            row = {
                "city": city,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "aqi": data['main']['aqi'],  # 1=Good, 5=Very Poor
                "co": components.get('co'),
                "no2": components.get('no2'),
                "o3": components.get('o3'),
                "pm2_5": components.get('pm2_5')
            }
            results.append(row)
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch data for {city}: {e}")

    if results:
        df = pd.DataFrame(results)
        print("\n--- LIVE AIR QUALITY DATA ---")
        print(df.to_string(index=False)) # Pretty print the table
        return df
    else:
        print("⚠️ No data collected.")
        return None

if __name__ == "__main__":
    fetch_air_quality()
