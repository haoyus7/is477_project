# Interim Status Report
## The Impact of Inflation on U.S. Consumer Spending (2015–2024)

### 1. Project Overview
This project investigates how inflation has influenced consumer spending behavior in the United States from 2015 through 2024. Using official data from the Federal Reserve Economic Data (FRED) system, we examine the statistical relationship between the Consumer Price Index (CPIAUCSL) and Personal Consumption Expenditures (PCE). The primary goal is to determine how increases in inflation correspond to changes in real consumer spending after adjusting for price level effects.

The study adopts a full data lifecycle approach, from acquisition and cleaning to integration, quality assessment, and documentation. By building reproducible workflows in Python, we aim to create an end-to-end data pipeline that can automatically regenerate our analysis-ready dataset. The findings will inform our later exploratory and modeling stages, supporting our central research questions:

- How has rising inflation since 2020 affected real consumer spending in the United States?
- What is the statistical relationship between inflation (CPI) and total personal consumption expenditures (PCE)?
- Does the effect of inflation on spending appear immediately, or does it occur with a time lag?

### 2. Progress Update

#### 2.1 Data Acquisition
Both datasets—CPIAUCSL (Consumer Price Index for All Urban Consumers) and PCE (Personal Consumption Expenditures)—have been successfully acquired from the FRED platform.

CPIAUCSL was retrieved programmatically using the FRED API. The API key was stored securely in a fred_api_key.txt file and excluded from version control via .gitignore. The raw CSV file and accompanying metadata (CPIAUCSL.csv, CPIAUCSL_metadata.json) are saved in data/raw/.

PCE was downloaded through FRED’s bulk data CSV interface at https://fred.stlouisfed.org/series/PCE/downloaddata/PCE.csv. This method was chosen over the API to ensure reliability and avoid API throttling or network timeout errors. Metadata (PCE_metadata.json) records the retrieval time, source URL, and checksum for reproducibility.

Resulting Files:
- data/raw/CPIAUCSL.csv
- data/raw/CPIAUCSL_metadata.json
- data/raw/PCE.csv
- data/raw/PCE_metadata.json

Each dataset includes approximately 120 monthly observations spanning January 2015 – December 2024.

#### 2.2 Data Integration
The CPI and PCE datasets were aligned by their shared date column and merged into a unified file, macro_monthly.csv, using Pandas. The merged dataset contains three core variables:

date: Monthly observation date (YYYY-MM-DD)
cpi: CPIAUCSL level (index value)
pce: Personal Consumption Expenditures, billions of chained 2017 USD

The integration produced 120 consistent monthly observations, with a one-to-one match on every date. Duplicate detection confirmed no overlapping or mismatched records.

Artifacts created:
- data/processed/macro_monthly.csv
- data/processed/macro_monthly_metadata.json

#### 2.3 Feature Extraction and Enrichment
Following integration, several analytical variables were derived to enhance interpretability:

- CPI Index (2015-01 = 100) — CPI values were normalized to 100 at January 2015 to establish a consistent base year for comparison.
- Real PCE — Nominal PCE values were deflated using the CPI index, yielding inflation-adjusted consumer spending.
- Year-over-Year (YoY) Growth Rates — For CPI, nominal PCE, and real PCE, 12-month percentage changes were calculated.

These transformations provide the basis for assessing both nominal and real trends in consumer spending, as well as inflation momentum.

Resulting columns: ['date', 'cpi', 'pce', 'cpi_index_2015_01_100', 'real_pce', 'pce_yoy_pct', 'real_pce_yoy_pct', 'cpi_yoy_pct']

#### 2.4 Data Quality and Cleaning
Data quality checks were completed using systematic profiling scripts:

Missing values: 0 for all base columns; 12 NAs in YoY columns (expected for first 12 months)
Duplicate dates: 0
Date coverage: 2015-01-01 → 2024-12-01
Numeric validation: All CPI > 0 and PCE > 0

QC Summary (from notebook):
{'missing_counts': {'date': 0, 'cpi': 0, 'pce': 0, 'cpi_index_2015_01_100': 0, 'real_pce': 0, 'pce_yoy_pct': 12, 'real_pce_yoy_pct': 12, 'cpi_yoy_pct': 12}, 'date_min': '2015-01-01', 'date_max': '2024-12-01', 'duplicate_dates': 0}

All quality control steps confirm that the integrated dataset is consistent, continuous, and analysis-ready.

#### 2.5 Documentation and Metadata
Comprehensive documentation has been created in the docs/ folder:

- data_dictionary.md — defines all variables, units, and transformations.
- qc_summary.json — records data integrity checks and date coverage.
- requirements.txt — lists all dependencies required to reproduce the workflow (pandas, requests, matplotlib, urllib3, etc.).
- README.md (in progress) — will summarize reproduction steps for the final submission.

All metadata files include UTC timestamps, SHA-256 checksums, and source attribution to ensure traceability and compliance with reproducibility guidelines.

#### 2.6 Current Repository Structure
interim_report/
  data/
    raw/
      CPIAUCSL.csv
      CPIAUCSL_metadata.json
      PCE.csv
      PCE_metadata.json
    processed/
      macro_monthly.csv
      macro_monthly_metadata.json
  scripts/
    acquire_data.ipynb
  fred_api_key.txt (ignored)
  requirements.txt
  .gitignore

### 3. Updated Timeline
Task and Status:
Data acquisition (CPI, PCE): Completed Oct 31
Storage & organization: Completed Nov 3
Extraction & enrichment: Completed Nov 5
Integration (CPI + PCE): Completed Nov 5
Data quality & cleaning: Completed Nov 6
Workflow automation: In progress
Exploratory Data Analysis: Scheduled
Modeling & analysis: Scheduled
Documentation & metadata: Ongoing
Final report submission: Planned

The project remains on schedule. Core data lifecycle tasks are complete; upcoming work focuses on automation, exploratory visualizations, and regression analysis.

### 4. Changes to the Plan
- PCE data acquisition method changed from API to bulk CSV for reliability.
- Workflow automation was restructured to begin in Jupyter, then export to scripts.
- Metadata tracking was expanded to include SHA-256 hash validation and UTC timestamps.
- SQL integration was removed since Pandas handled time-series merging efficiently.

### 5. Challenges and Resolutions
- API access issues: Fixed by cleaning hidden characters in API key and verifying requests.
- Network errors: Resolved by retry logic and switching to CSV endpoint.
- Argument parsing conflicts: Adjusted notebook structure to avoid CLI issues.
- Data alignment: Truncated datasets to common date index for uniform range.
- Reproducibility: Added metadata with checksums and timestamps.

### 6. Individual Contributions
Haoyu Shi:
- Designed folder structure.
- Implemented acquisition, integration, cleaning, and feature engineering.
- Authored metadata and QC documentation.
- Managed GitHub repository setup.

Bingqing Li:
- Reviewed transformation logic.
- Planned exploratory visualizations.
- Outlined regression models for lagged inflation effects.
- Will lead analytical interpretation and visualization in final phase.

### 7. Next Steps
- Automate pipeline (scripts: acquire_data.py, process_data.py, run_all.py).
- Conduct exploratory data analysis and visualization.
- Implement regression and lag models to evaluate inflation effects.
- Finalize documentation and metadata.
- Prepare final submission and GitHub release.

### 8. Summary
The project is progressing according to schedule and meets all requirements for reproducibility, transparency, and ethical data handling. The foundational data pipeline is complete: CPI and PCE have been successfully integrated, cleaned, and transformed into an analysis-ready dataset. Documentation and metadata ensure traceability, while the next phase will focus on analytical interpretation and workflow automation.

This interim milestone demonstrates a functional, replicable foundation for analyzing how inflation shapes real consumer spending in the United States—a topic of enduring economic and policy relevance.
