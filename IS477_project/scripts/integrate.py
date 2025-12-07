"""
Integrate and enrich CPI and PCE data.
Merges datasets and creates derived analytical variables.
"""

import argparse
from pathlib import Path

import pandas as pd

from utils import save_metadata, load_config


def integrate_data(cpi_path, pce_path):
    """Merge CPI and PCE datasets on date."""
    
    print(f"Loading CPI data from: {cpi_path}")
    cpi_df = pd.read_csv(cpi_path, parse_dates=['date'])
    
    print(f"Loading PCE data from: {pce_path}")
    pce_df = pd.read_csv(pce_path, parse_dates=['date'])
    
    # Merge on date (inner join)
    print("Merging datasets...")
    merged = pd.merge(cpi_df, pce_df, on='date', how='inner')
    merged = merged.sort_values('date').reset_index(drop=True)
    
    print(f"Merged dataset: {len(merged)} rows")
    return merged


def enrich_data(df, base_date="2015-01-01"):
    """Create derived analytical variables."""
    
    print("Creating derived variables...")
    
    # 1. CPI Index (base_date = 100)
    base_cpi = df.loc[df['date'] == base_date, 'cpi'].iloc[0]
    df['cpi_index_2015_01_100'] = (df['cpi'] / base_cpi) * 100
    print(f"  - cpi_index_2015_01_100 (base CPI: {base_cpi:.3f})")
    
    # 2. Real PCE (inflation-adjusted)
    df['real_pce'] = df['pce'] / (df['cpi_index_2015_01_100'] / 100)
    print("  - real_pce (inflation-adjusted)")
    
    # 3. Year-over-year growth rates
    df['pce_yoy_pct'] = df['pce'].pct_change(12) * 100
    df['real_pce_yoy_pct'] = df['real_pce'].pct_change(12) * 100
    df['cpi_yoy_pct'] = df['cpi'].pct_change(12) * 100
    print("  - pce_yoy_pct, real_pce_yoy_pct, cpi_yoy_pct (12-month lag)")
    
    return df


def main():
    parser = argparse.ArgumentParser(description='Integrate and enrich CPI/PCE data')
    parser.add_argument('--config', default='config.yaml', help='Path to config file')
    parser.add_argument('--cpi', required=True, help='Input CPI CSV path')
    parser.add_argument('--pce', required=True, help='Input PCE CSV path')
    parser.add_argument('--output', required=True, help='Output CSV path')
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Integrate data
    merged = integrate_data(args.cpi, args.pce)
    
    # Enrich data
    enriched = enrich_data(merged, config['cpi_base_date'])
    
    # Save output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    enriched.to_csv(output_path, index=False)
    print(f"Integrated data saved: {output_path}")
    
    # Save metadata
    save_metadata(output_path, {
        'description': 'Integrated CPI and PCE data with derived variables',
        'sources': ['CPIAUCSL (FRED API)', 'PCE (FRED CSV)'],
        'row_count': len(enriched),
        'columns': list(enriched.columns),
        'derived_variables': {
            'cpi_index_2015_01_100': 'CPI normalized to 2015-01 = 100',
            'real_pce': 'Inflation-adjusted PCE (2015 dollars)',
            'pce_yoy_pct': 'YoY % change in nominal PCE',
            'real_pce_yoy_pct': 'YoY % change in real PCE',
            'cpi_yoy_pct': 'YoY % change in CPI (inflation rate)'
        }
    })


if __name__ == '__main__':
    main()
