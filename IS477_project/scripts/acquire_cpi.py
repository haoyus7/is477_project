"""
Acquire CPI data from FRED API.
Downloads Consumer Price Index for All Urban Consumers (CPIAUCSL).
"""

import re
import argparse
from pathlib import Path

import pandas as pd

from utils import create_session, save_metadata, load_config


def load_api_key(api_key_file):
    """Load and clean FRED API key from file."""
    api_key = Path(api_key_file).read_text(encoding='utf-8-sig').strip()
    # Clean up (remove quotes, spaces, etc.)
    api_key = re.sub(r'\s+', '', api_key.strip('"').strip("'"))
    return api_key


def acquire_cpi(config, api_key):
    """Download CPI data from FRED API."""
    
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        'series_id': config['series']['cpi']['series_id'],
        'api_key': api_key,
        'file_type': 'json',
        'observation_start': config['start_date'],
        'observation_end': config['end_date'],
    }
    
    print(f"Fetching CPI data from FRED API...")
    session = create_session()
    response = session.get(url, params=params, timeout=60)
    response.raise_for_status()
    
    # Parse data
    data = response.json()['observations']
    cpi_df = pd.DataFrame(data)[['date', 'value']]
    cpi_df['date'] = pd.to_datetime(cpi_df['date'])
    cpi_df['value'] = pd.to_numeric(cpi_df['value'])
    cpi_df = cpi_df.rename(columns={'value': 'cpi'})
    
    return cpi_df


def main():
    parser = argparse.ArgumentParser(description='Acquire CPI data from FRED API')
    parser.add_argument('--config', default='config.yaml', help='Path to config file')
    parser.add_argument('--output', required=True, help='Output CSV path')
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Load API key
    api_key = load_api_key(config['fred_api_key_file'])
    
    # Acquire data
    cpi_df = acquire_cpi(config, api_key)
    
    # Save CSV
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cpi_df.to_csv(output_path, index=False)
    print(f"CPI data saved: {output_path} ({len(cpi_df)} rows)")
    
    # Save metadata
    save_metadata(output_path, {
        'series_id': config['series']['cpi']['series_id'],
        'source': config['series']['cpi']['source'],
        'description': config['series']['cpi']['description'],
        'row_count': len(cpi_df),
    })


if __name__ == '__main__':
    main()
