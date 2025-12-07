# Data Dictionary

## Project: The Impact of Inflation on U.S. Consumer Spending (2015–2024)

This document provides detailed descriptions of all variables in the datasets used for this project.

---

## Raw Datasets

### CPIAUCSL.csv

**Source**: Federal Reserve Economic Data (FRED), U.S. Bureau of Labor Statistics  
**Frequency**: Monthly  
**Time Period**: January 2015 – December 2024  
**Observations**: 120  

| Variable | Data Type | Description | Units |
|----------|-----------|-------------|-------|
| `date` | Date (YYYY-MM-DD) | First day of the month for which the observation applies | - |
| `cpi` | Float | Consumer Price Index for All Urban Consumers: All Items in U.S. City Average | Index (1982-84=100) |

**Notes**: The CPI measures the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services. Values are not seasonally adjusted.

---

### PCE.csv

**Source**: Federal Reserve Economic Data (FRED), U.S. Bureau of Economic Analysis  
**Frequency**: Monthly  
**Time Period**: January 2015 – December 2024  
**Observations**: 120  

| Variable | Data Type | Description | Units |
|----------|-----------|-------------|-------|
| `date` | Date (YYYY-MM-DD) | First day of the month for which the observation applies | - |
| `pce` | Float | Personal Consumption Expenditures | Billions of Dollars |

**Notes**: PCE measures the value of goods and services purchased by (or on behalf of) U.S. residents. Values are seasonally adjusted at annual rates.

---

## Processed Dataset

### macro_monthly.csv

**Source**: Derived from CPIAUCSL.csv and PCE.csv  
**Frequency**: Monthly  
**Time Period**: January 2015 – December 2024  
**Observations**: 120  

| Variable | Data Type | Description | Units | Derivation |
|----------|-----------|-------------|-------|------------|
| `date` | Date (YYYY-MM-DD) | First day of the month | - | From source data |
| `cpi` | Float | Consumer Price Index | Index (1982-84=100) | From CPIAUCSL.csv |
| `pce` | Float | Personal Consumption Expenditures (nominal) | Billions of Dollars | From PCE.csv |
| `cpi_index_2015_01_100` | Float | CPI normalized to January 2015 = 100 | Index (2015-01=100) | `(cpi / 234.747) × 100` |
| `real_pce` | Float | Inflation-adjusted PCE in constant 2015 dollars | Billions of 2015 Dollars | `pce / (cpi_index_2015_01_100 / 100)` |
| `pce_yoy_pct` | Float | Year-over-year percentage change in nominal PCE | Percent | `((pce_t - pce_{t-12}) / pce_{t-12}) × 100` |
| `real_pce_yoy_pct` | Float | Year-over-year percentage change in real PCE | Percent | `((real_pce_t - real_pce_{t-12}) / real_pce_{t-12}) × 100` |
| `cpi_yoy_pct` | Float | Year-over-year percentage change in CPI (inflation rate) | Percent | `((cpi_t - cpi_{t-12}) / cpi_{t-12}) × 100` |

**Notes on Missing Values**:
- The variables `pce_yoy_pct`, `real_pce_yoy_pct`, and `cpi_yoy_pct` have 12 missing values for the first 12 months (January 2015 – December 2015) because year-over-year calculations require data from the previous year.
- This is expected behavior and not a data quality issue.

---

## Variable Definitions

### Consumer Price Index (CPI)

The Consumer Price Index measures the average change over time in the prices paid by urban consumers for a representative basket of consumer goods and services. The CPI is calculated by the U.S. Bureau of Labor Statistics and is one of the most widely used measures of inflation.

**Base Period**: The index is set so that the average value during 1982-1984 equals 100.

### Personal Consumption Expenditures (PCE)

Personal Consumption Expenditures measures the value of goods and services purchased by households and nonprofit institutions serving households. It is the primary measure of consumer spending in the U.S. national accounts and is calculated by the Bureau of Economic Analysis.

**Adjustment**: The PCE values in this dataset are seasonally adjusted at annual rates.

### Real PCE

Real PCE adjusts nominal PCE for inflation, expressing consumer spending in constant dollars. This allows comparison of spending across time periods without the confounding effect of price changes.

**Base Period**: January 2015 (the beginning of our study period)

**Formula**: Real PCE = Nominal PCE / (CPI Index / 100)

### Year-over-Year Percentage Change

Year-over-year (YoY) percentage change compares a value to its level 12 months prior. This approach removes seasonal effects and provides a measure of annual growth or decline.

**Formula**: YoY % = ((Value_t - Value_{t-12}) / Value_{t-12}) × 100

---

## Data Quality Summary

| Check | Result | Notes |
|-------|--------|-------|
| Missing values (core variables) | Pass | No missing values in date, cpi, pce |
| Missing values (derived variables) | Expected | 12 missing values in YoY variables for first year |
| Duplicate dates | Pass | No duplicate dates found |
| Temporal coverage | Pass | Complete monthly coverage, no gaps |
| Value ranges | Pass | All values within expected economic ranges |

---

## File Checksums

SHA-256 checksums for data integrity verification:

| File | SHA-256 |
|------|---------|
| CPIAUCSL.csv | See CPIAUCSL_metadata.json |
| PCE.csv | See PCE_metadata.json |
| macro_monthly.csv | See macro_monthly_metadata.json |

---

## Contact

For questions about this data dictionary, contact:
- Haoyu Shi (haoyu@illinois.edu)
- Bingqing (bingqing@illinois.edu)
