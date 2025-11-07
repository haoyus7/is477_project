import requests
import pandas as pd
import json
import hashlib
from datetime import datetime
import os
import time

# Configuration
SERIES_ID = "PCE"
START_DATE = "2015-01-01"
END_DATE = "2024-12-31"
OUTPUT_DIR = "../data/raw"
OUTPUT_FILE = "pce_data_download.csv"

# FRED's direct CSV download URL
csv_url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={SERIES_ID}"

def download_pce_data_method1():
    
    params = {
        'cosd': START_DATE,  
        'coed': END_DATE     
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # Download the CSV file
        response = requests.get(csv_url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Write the raw content to file (similar to Chicago towing example)
        output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        with open(output_path, "wb") as f:
            f.write(response.content)
        
        # Read the saved CSV file to verify
        df = pd.read_csv(output_path)
        
        return df, response
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Download failed: {str(e)}")
        return None, None


def verify_and_display_data(df, method_name):
    """
    Verify data integrity and display summary
    """
    if df is None:
        return
    
    print(f"\n--- {method_name} Data Summary ---")
    
    # Check for missing values
    missing_count = df.iloc[:, 1].isna().sum() if len(df.columns) > 1 else 0
    print(f"Missing values: {missing_count}")
    
    # Display basic info
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    # Show first and last rows
    print("\nFirst 3 rows:")
    print(df.head(3))
    print("\nLast 3 rows:")
    print(df.tail(3))

def calculate_checksum(filepath):
    """Calculate SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def save_metadata(df, response, method, filepath):
    """Save metadata about the downloaded data."""
    metadata = {
        'series_id': SERIES_ID,
        'source': 'FRED Website',
        'access_method': method,
        'download_date': datetime.now().isoformat(),
        'start_date': START_DATE,
        'end_date': END_DATE,
        'num_observations': len(df) if df is not None else 0,
        'download_url': csv_url,
        'status_code': response.status_code if response else None,
        'file_checksum_sha256': calculate_checksum(filepath) if os.path.exists(filepath) else None,
        'manual_download_instructions': [
            f'1. Visit https://fred.stlouisfed.org/series/{SERIES_ID}',
            '2. Click the "Download" button',
            '3. Select "CSV" format',
            '4. Save the file to data/raw/'
        ]
    }
    
    metadata_file = filepath.replace('.csv', '_metadata.json')
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Metadata saved to: {metadata_file}")

def main():
    """Main execution function."""
    print("PCE Data Download Script")
    print("========================\n")
    
    # Method 1: Direct download and save (Chicago towing style)
    df1, response1 = download_pce_data_method1()
    if df1 is not None:
        verify_and_display_data(df1, "Method 1")
        output_path1 = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        save_metadata(df1, response1, "Direct Download", output_path1)
    
if __name__ == "__main__":
    main()
