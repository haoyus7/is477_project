import requests
import pandas as pd
import json
import hashlib
from datetime import datetime
import os

# Configuration
FRED_API_KEY = "Your FRED API Key"  # Replace with your actual API key
SERIES_ID = "CPIAUCSL"
START_DATE = "2015-01-01"
END_DATE = "2024-12-31"
OUTPUT_DIR = "../data/raw"
OUTPUT_FILE = "cpi_data_api.csv"

def fetch_fred_data(series_id, api_key, start_date, end_date):
    """
    Fetch data from FRED API.
    series_id : FRED series identifier
    api_key : Your FRED API key
    start_date : Start date in YYYY-MM-DD format
    end_date : End date in YYYY-MM-DD format
    """
    base_url = "https://api.stlouisfed.org/fred/series/observations"
    
    params = {
        'series_id': series_id,
        'api_key': api_key,
        'file_type': 'json',
        'observation_start': start_date,
        'observation_end': end_date
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        observations = data['observations']
        
        # Convert to DataFrame
        df = pd.DataFrame(observations)
        df['date'] = pd.to_datetime(df['date'])
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        
        print(f"Successfully fetched {len(df)} observations")
        return df[['date', 'value']]
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def calculate_checksum(filepath):
    """Calculate SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def save_metadata(df, filepath, checksum):
    metadata = {
        'series_id': SERIES_ID,
        'source': 'FRED API',
        'access_method': 'API',
        'download_date': datetime.now().isoformat(),
        'start_date': START_DATE,
        'end_date': END_DATE,
        'num_observations': len(df),
        'file_checksum_sha256': checksum,
        'api_url': 'https://api.stlouisfed.org/fred/series/observations'
    }
    
    metadata_file = filepath.replace('.csv', '_metadata.json')
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Metadata saved to {metadata_file}")

def main():
    """Main execution function."""
    # Check if API key is set
    if FRED_API_KEY == "YOUR_API_KEY_HERE":
        print("ERROR: Please set your FRED API key in the script!")
        print("Get your free API key at: https://fred.stlouisfed.org/docs/api/api_key.html")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Fetch data
    try:
        df = fetch_fred_data(SERIES_ID, FRED_API_KEY, START_DATE, END_DATE)
        
        # Rename columns for clarity
        df.columns = ['date', 'cpi']
        
        # Save to CSV
        output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
        
        # Calculate checksum
        checksum = calculate_checksum(output_path)
        print(f"File checksum (SHA-256): {checksum}")
        
        # Save metadata
        save_metadata(df, output_path, checksum)

        print(df.head())
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
  
