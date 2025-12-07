"""
Data quality assessment for the integrated dataset.
Checks for missing values, duplicates, and temporal coverage.
"""

import argparse
import json
from pathlib import Path

import pandas as pd


def run_quality_checks(df):
    """Run comprehensive quality checks on the dataset."""
    
    results = {
        'status': 'PASS',
        'checks': {},
        'warnings': [],
        'errors': []
    }
    
    print("=" * 60)
    print("DATA QUALITY ASSESSMENT")
    print("=" * 60)
    
    # 1. Missing Values Check
    print("\n1. Missing Values Check")
    print("-" * 40)
    missing = df.isna().sum()
    missing_info = {}
    
    for col, count in missing.items():
        if count > 0:
            missing_info[col] = int(count)
            if '_yoy_' in col:
                print(f"   {col}: {count} missing (OK - first 12 months)")
            else:
                print(f"   {col}: {count} missing (WARNING)")
                results['warnings'].append(f"{col} has {count} missing values")
        else:
            print(f"   {col}: OK (no missing)")
    
    results['checks']['missing_values'] = missing_info
    
    # 2. Duplicate Dates Check
    print("\n2. Duplicate Dates Check")
    print("-" * 40)
    duplicates = df.duplicated('date').sum()
    results['checks']['duplicate_dates'] = int(duplicates)
    
    if duplicates == 0:
        print(f"   OK: No duplicate dates found")
    else:
        print(f"   ERROR: {duplicates} duplicate dates found")
        results['errors'].append(f"{duplicates} duplicate dates")
        results['status'] = 'FAIL'
    
    # 3. Temporal Coverage Check
    print("\n3. Temporal Coverage Check")
    print("-" * 40)
    date_range = {
        'start': str(df['date'].min().date()),
        'end': str(df['date'].max().date()),
        'total_months': len(df)
    }
    results['checks']['date_range'] = date_range
    
    print(f"   Start: {date_range['start']}")
    print(f"   End: {date_range['end']}")
    print(f"   Total observations: {date_range['total_months']}")
    
    # Check for gaps
    df_sorted = df.sort_values('date')
    date_diffs = df_sorted['date'].diff().dropna()
    expected_diff = pd.Timedelta(days=28)  # Approximately 1 month
    max_diff = date_diffs.max()
    
    if max_diff > pd.Timedelta(days=35):
        results['warnings'].append(f"Potential gap detected: max interval is {max_diff.days} days")
        print(f"   WARNING: Max interval between dates is {max_diff.days} days")
    else:
        print(f"   OK: No gaps detected (max interval: {max_diff.days} days)")
    
    # 4. Value Range Check
    print("\n4. Value Range Check")
    print("-" * 40)
    
    range_checks = {
        'cpi': {'min': 100, 'max': 500},
        'pce': {'min': 1000, 'max': 30000},
    }
    
    for col, bounds in range_checks.items():
        if col in df.columns:
            col_min = df[col].min()
            col_max = df[col].max()
            
            if col_min >= bounds['min'] and col_max <= bounds['max']:
                print(f"   {col}: OK (range: {col_min:.2f} - {col_max:.2f})")
            else:
                print(f"   {col}: WARNING (range: {col_min:.2f} - {col_max:.2f})")
                results['warnings'].append(f"{col} has unexpected range")
    
    # 5. Summary
    print("\n" + "=" * 60)
    print(f"OVERALL STATUS: {results['status']}")
    if results['warnings']:
        print(f"Warnings: {len(results['warnings'])}")
    if results['errors']:
        print(f"Errors: {len(results['errors'])}")
    print("=" * 60)
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Run data quality checks')
    parser.add_argument('--input', required=True, help='Input CSV path')
    parser.add_argument('--output', required=True, help='Output JSON report path')
    args = parser.parse_args()
    
    # Load data
    print(f"Loading data from: {args.input}")
    df = pd.read_csv(args.input, parse_dates=['date'])
    
    # Run quality checks
    results = run_quality_checks(df)
    
    # Save report
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, indent=2))
    print(f"\nQuality report saved: {output_path}")
    
    # Exit with error code if checks failed
    if results['status'] == 'FAIL':
        exit(1)


if __name__ == '__main__':
    main()
