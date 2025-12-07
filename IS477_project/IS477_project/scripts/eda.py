"""
Exploratory Data Analysis for Inflation & Consumer Spending.
Generates visualizations, correlation analysis, and descriptive statistics.
"""

import argparse
import json
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_inflation_over_time(df, output_path):
    """Plot CPI year-over-year inflation rate over time."""
    plt.figure(figsize=(14, 6))
    
    # Filter to only rows with YoY data (after first 12 months)
    plot_df = df.dropna(subset=['cpi_yoy_pct'])
    
    plt.plot(plot_df['date'], plot_df['cpi_yoy_pct'], 
             color='#1f77b4', linewidth=2, label='Inflation (CPI YoY %)')
    
    plt.title('Inflation Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('CPI Year-over-Year (%)', fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")


def plot_pce_trends(df, output_path):
    """Plot nominal and real PCE trends over time."""
    plt.figure(figsize=(14, 6))
    
    plt.plot(df['date'], df['pce'], 
             color='#1f77b4', linewidth=2, label='Nominal PCE')
    plt.plot(df['date'], df['real_pce'], 
             color='#ff7f0e', linewidth=2, label='Real PCE')
    
    plt.title('Trends in PCE (2015-2024)', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")


def plot_growth_rates(df, output_path):
    """Plot year-over-year growth rates for CPI and PCE."""
    plt.figure(figsize=(14, 6))
    
    # Filter to only rows with YoY data
    plot_df = df.dropna(subset=['cpi_yoy_pct', 'pce_yoy_pct', 'real_pce_yoy_pct'])
    
    plt.plot(plot_df['date'], plot_df['cpi_yoy_pct'], 
             color='#1f77b4', linewidth=2, label='CPI YoY %')
    plt.plot(plot_df['date'], plot_df['pce_yoy_pct'], 
             color='#ff7f0e', linewidth=2, label='Nominal PCE YoY %')
    plt.plot(plot_df['date'], plot_df['real_pce_yoy_pct'], 
             color='#2ca02c', linewidth=2, label='Real PCE YoY %')
    
    plt.title('Year-over-Year Growth Rates (2015-2024)', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('YoY Growth (%)', fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")


def plot_correlation_matrix(df, output_path):
    """Plot correlation matrix heatmap for growth rate variables."""
    # Select YoY columns for correlation
    corr_cols = ['cpi_yoy_pct', 'pce_yoy_pct', 'real_pce_yoy_pct']
    corr_df = df[corr_cols].dropna()
    
    # Calculate correlation matrix
    corr_matrix = corr_df.corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='Reds', center=0,
                fmt='.2f', square=True, linewidths=0.5,
                vmin=-1, vmax=1)
    
    plt.title('Correlation Matrix: CPI vs PCE Growth Rates', 
              fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")


def compute_descriptive_stats(df, output_path):
    """Compute and save descriptive statistics."""
    # Select columns for statistics
    stats_cols = ['cpi_yoy_pct', 'pce_yoy_pct', 'real_pce_yoy_pct']
    stats_df = df[stats_cols].dropna()
    
    # Compute statistics
    stats = stats_df.describe()
    
    # Add additional statistics
    stats.loc['skew'] = stats_df.skew()
    stats.loc['kurtosis'] = stats_df.kurtosis()
    
    # Save to CSV
    stats.to_csv(output_path)
    print(f"Saved: {output_path}")
    
    # Print to console
    print("\n" + "=" * 60)
    print("DESCRIPTIVE STATISTICS")
    print("=" * 60)
    print(stats.round(4).to_string())
    
    return stats


def compute_correlation_analysis(df, output_path):
    """Compute and save correlation analysis."""
    # Select columns for correlation
    corr_cols = ['cpi_yoy_pct', 'pce_yoy_pct', 'real_pce_yoy_pct']
    corr_df = df[corr_cols].dropna()
    
    # Calculate correlation matrix
    corr_matrix = corr_df.corr()
    
    # Save to CSV
    corr_matrix.to_csv(output_path)
    print(f"Saved: {output_path}")
    
    # Print to console
    print("\n" + "=" * 60)
    print("CORRELATION MATRIX")
    print("=" * 60)
    print(corr_matrix.round(4).to_string())
    
    # Key finding
    cpi_real_pce_corr = corr_matrix.loc['cpi_yoy_pct', 'real_pce_yoy_pct']
    print(f"\nKey Finding: Correlation between inflation and real PCE growth: {cpi_real_pce_corr:.4f}")
    
    return corr_matrix


def main():
    parser = argparse.ArgumentParser(description='Run exploratory data analysis')
    parser.add_argument('--input', required=True, help='Input CSV path')
    parser.add_argument('--output-dir', required=True, help='Output directory for results')
    args = parser.parse_args()
    
    # Create output directories
    output_dir = Path(args.output_dir)
    figures_dir = output_dir / 'figures'
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    # Load data
    print(f"Loading data from: {args.input}")
    df = pd.read_csv(args.input, parse_dates=['date'])
    print(f"Loaded {len(df)} observations")
    
    print("\n" + "=" * 60)
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 60)
    
    # Generate visualizations
    print("\nGenerating visualizations...")
    plot_inflation_over_time(df, figures_dir / 'inflation_over_time.png')
    plot_pce_trends(df, figures_dir / 'pce_trends.png')
    plot_growth_rates(df, figures_dir / 'growth_rates.png')
    plot_correlation_matrix(df, figures_dir / 'correlation_matrix.png')
    
    # Compute statistics
    print("\nComputing statistics...")
    compute_descriptive_stats(df, output_dir / 'descriptive_stats.csv')
    compute_correlation_analysis(df, output_dir / 'correlation_matrix.csv')
    
    # Save EDA summary
    eda_summary = {
        'input_file': args.input,
        'total_observations': len(df),
        'date_range': {
            'start': str(df['date'].min().date()),
            'end': str(df['date'].max().date())
        },
        'outputs': {
            'figures': [
                'figures/inflation_over_time.png',
                'figures/pce_trends.png',
                'figures/growth_rates.png',
                'figures/correlation_matrix.png'
            ],
            'statistics': [
                'descriptive_stats.csv',
                'correlation_matrix.csv'
            ]
        }
    }
    
    summary_path = output_dir / 'eda_summary.json'
    summary_path.write_text(json.dumps(eda_summary, indent=2))
    print(f"\nSaved: {summary_path}")
    
    print("\n" + "=" * 60)
    print("EDA COMPLETE")
    print("=" * 60)


if __name__ == '__main__':
    main()
