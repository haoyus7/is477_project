"""
Acquire PCE data from FRED CSV download.
Downloads Personal Consumption Expenditures (PCE).
"""

import argparse
import io
from pathlib import Path

import pandas as pd

from utils import create_session, save_metadata, load_config


def acquire_pce(config):
    """Download PCE data from FRED website CSV."""
    
    # Try multiple URLs (fallback approach)
    urls = [
        f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={config['series']['pce']['series_id']}",
        f"https://fred.stlouisfed.org/series/{config['series']['pce']['series_id']}/downloaddata/{config['series']['pce']['series_id']}.csv",
    ]
    
    session = create_session()
    pce_df = None
    successful_url = None
    
    for url in urls:
        try:
            print(f"Trying: {url}")
            response = session.get(url, timeout=60)
            response.raise_for_status()
            
            # Parse CSV
            pce_df = pd.read_csv(io.StringIO(response.text))
            successful_url = url
            print(f"Downloaded from: {url}")
            break
        except Exception as e:
            print(f"Failed: {url} - {e}")
            continue
    
    if pce_df is None:
        raise RuntimeError("Failed to download PCE data from all URLs")
    
    # Standardize column names
    pce_df.columns = pce_df.columns.str.lower()
    if 'date' not in pce_df.columns:
        pce_df = pce_df.rename(columns={pce_df.columns[0]: 'date'})
    
    # Rename value column
    value_col = [c for c in pce_df.columns if c != 'date'][0]
    pce_df = pce_df.rename(columns={value_col: 'pce'})
    
    # Parse dates and filter
    pce_df['date'] = pd.to_datetime(pce_df['date'])
    start = pd.to_datetime(config['start_date'])
    end = pd.to_datetime(config['end_date'])
    pce_df = pce_df[(pce_df['date'] >= start) & (pce_df['date'] <= end)]
    pce_df = pce_df.sort_values('date').reset_index(drop=True)
    
    return pce_df


def main():
    parser = argparse.ArgumentParser(description='Acquire PCE data from FRED CSV')
    parser.add_argument('--config', default='config.yaml', help='Path to config file')
    parser.add_argument('--output', required=True, help='Output CSV path')
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Acquire data
    pce_df = acquire_pce(config)
    
    # Save CSV
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pce_df.to_csv(output_path, index=False)
    print(f"PCE data saved: {output_path} ({len(pce_df)} rows)")
    
    # Save metadata
    save_metadata(output_path, {
        'series_id': config['series']['pce']['series_id'],
        'source': config['series']['pce']['source'],
        'description': config['series']['pce']['description'],
        'row_count': len(pce_df),
    })


if __name__ == '__main__':
    main()
