# Interim Status Report

**Project**: The Impact of Inflation on U.S. Consumer Spending (2015–2024)  
**Team Members**: Haoyu, Bingqing  
**Date**: November 11, 2025  

---

## Executive Summary

We have completed the data acquisition, integration, enrichment, and quality assessment phases of our project. Both CPI and PCE datasets covering 2015-2024 have been successfully retrieved from FRED, merged into a unified time series, and enriched with analytical variables. Data quality assessment confirms the dataset is ready for analysis. We are now positioned to begin exploratory data analysis and statistical modeling as planned.

---

## Progress on Project Plan Tasks

### Data Acquisition - Completed

**Timeline**: Planned October 20th, Completed 
**Responsible**: Haoyu

We successfully acquired both required datasets from FRED using two distinct access methods. The CPI data was retrieved via the FRED API using programmatic access with authentication. The PCE data was obtained through direct CSV download from the FRED website. Both datasets contain 120 monthly observations from January 2015 through December 2024.

**Key accomplishments**:
- Implemented FRED API access for CPI data with error handling and retry logic
- Developed CSV download mechanism for PCE data with fallback URLs
- Generated SHA-256 checksums for all downloaded files to verify data integrity
- Created comprehensive metadata files documenting sources and retrieval information

**Files created**:
- `data/raw/CPIAUCSL.csv` - CPI dataset (120 observations)
- `data/raw/CPIAUCSL_metadata.json` - CPI documentation
- `data/raw/PCE.csv` - PCE dataset (120 observations)
- `data/raw/PCE_metadata.json` - PCE documentation
- `acquire_data.ipynb` - Complete acquisition notebook

**Data Licensing and Terms of Use**

All data used in this project were obtained from the Federal Reserve Bank of St. Louis FRED database. According to the FRED Terms of Use, the data are publicly available for educational and research purposes without restriction(personal, non-commercial use), provided appropriate attribution is given. Accordingly, we will cite FRED as the data source in all documentation and visualizations. No proprietary or personally identifiable information is included in these datasets.

### Storage and Organization - Completed

**Timeline**: Planned October 25th, Completed
**Responsible**: Haoyu

We established an organized project structure with clear separation between raw and processed data. The directory structure includes dedicated folders for source data, processed outputs, and analysis scripts. File naming conventions follow consistent patterns that clearly indicate data content and processing stage.

**Project structure**:
- `data/raw/` - Original downloaded datasets
- `data/processed/` - Cleaned and integrated data
- `acquire_data.ipynb` - Data acquisition and processing notebook

### Data Integration - Completed

**Timeline**: Planned October 29th, Completed
**Responsible**: Haoyu

The CPI and PCE datasets were successfully merged into a single unified time series aligned by date. We used an inner join to ensure only complete observations are included, maintaining data quality throughout the integration process. The merge was validated to confirm no duplicate dates exist and that all 120 monthly observations are properly aligned.

**Integration results**:
- Successfully merged datasets using date as the key
- Maintained complete temporal coverage (120 months)
- Validated one-to-one date relationships
- Created `data/processed/macro_monthly.csv` with integrated data
- Generated metadata documenting integration methodology

### Extraction and Enrichment - Completed

**Timeline**: Planned October 27th, Completed
**Responsible**: Haoyu

We created five analytical variables to support our research questions about inflation's impact on consumer spending. The CPI was normalized to create an index with January 2015 as the base period. This index was then used to calculate real Personal Consumption Expenditures in constant 2015 dollars. Year-over-year growth rates were computed for all key variables using 12-month lags to enable analysis of annual trends.

**Variables created**:
- `cpi_index_2015_01_100` - CPI normalized to January 2015 = 100
- `real_pce` - Inflation-adjusted consumer spending in 2015 dollars
- `pce_yoy_pct` - Year-over-year percentage change in nominal PCE
- `real_pce_yoy_pct` - Year-over-year percentage change in real PCE
- `cpi_yoy_pct` - Year-over-year percentage change in CPI (inflation rate)

All derived variables are documented with calculation methods in the metadata files.

### Data Quality Assessment - Completed

**Timeline**: Planned November 1st, Completed
**Responsible**: Haoyu

We conducted comprehensive quality checks on the integrated dataset to identify any issues before proceeding with analysis. The assessment examined missing values, duplicate dates, temporal completeness, and value range validation.

**Quality assessment findings**:
- Core variables (date, CPI, PCE) have no missing values
- Year-over-year variables have 12 missing values in first year (expected)
- No duplicate dates found
- Complete monthly coverage with no gaps
- All values fall within reasonable economic ranges
- Dataset is ready for analysis with no cleaning required

The quality assessment results are documented in the processed data metadata file.

---

## Tasks Not Yet Started

### Workflow Automation

**Timeline**: Planned November 12th
**Responsible**: Haoyu

This task will involve creating an automated script to execute the complete data pipeline from acquisition through quality assessment. We plan to implement a Snakemake workflow for robust automation.

### Exploratory Data Analysis

**Timeline**: Planned November 14th  
**Responsible**: Bingqing

The exploratory data analysis (EDA) phase will focus on uncovering key trends and relationships between inflation and consumer spending over the 2015–2024 period. We will begin by generating some time series visualizations to examine temporal dynamics in both nominal and real Personal Consumption Expenditures (PCE) alongside the Consumer Price Index (CPI).

**Analyses may include**:

- Trend visualization: Line charts of and real PCE to identify inflationary periods and spending responses.
- Growth rate analysis: Examination of year-over-year changes to capture short-term and long-term fluctuations.
- Correlation analysis: Assessment of the linear relationship between CPI growth and both nominal and real PCE growth.
- Descriptive statistics: Summary measures (mean, variance, skewness, kurtosis) for key indicators to characterize their distributions and variability over time.

### Statistical Modeling

**Timeline**: Planned November 17th  
**Responsible**: Bingqing

Following the exploratory data analysis, the statistical modeling part will quantify the relationship between inflation and real consumer spending. We plan to employ multiple linear regression models, testing both contemporaneous and lagged effects of CPI on real PCE.

**Modeling objectives may include**:

- Estimating the sensitivity of real PCE growth to inflation (CPI year-over-year change)
- Testing for delayed effects by including lagged inflation terms (such as 3-month, 6-month, and 12-month lags)
- Evaluating model fit and robustness using diagnostic metrics (adjusted R², AIC, residual analysis)
- Assessing potential structural breaks, particularly around the COVID-19 pandemic period (2019–2022)

### Documentation and Final Report

**Timeline**: Planned November 20-28th  
**Responsible**: Both

The final stage of the project will focus on compiling and documenting all components of the data curation and analysis workflow. This phase will ensure that our project is fully transparent, reproducible, and well-organized for final submission.

**Key deliverables will include**:

- Comprehensive project report: A detailed summary of the research motivation, datasets, data quality assessment, analysis results, and conclusions following the project submission guidelines.
- Data dictionary and metadata: Documentation of all variables, their definitions, data sources, and transformation procedures.
- Workflow documentation: Step-by-step instructions describing how the end-to-end pipeline (from data acquisition to visualization) can be reproduced.
- Final outputs: All processed datasets, scripts, and visualization results stored in the project repository and linked to the shared folder for accessibility.

---

## Updated Timeline

| Task | Original Target | Status | Assigned To |
|------|----------------|--------|-------------|
| Data Acquisition | Oct 20 | Complete | Haoyu |
| Storage & Organization | Oct 25 | Complete | Haoyu |
| Extraction & Enrichment | Oct 27 | Complete | Haoyu |
| Data Integration | Oct 29 | Complete | Haoyu |
| Data Quality | Nov 1 | Complete | Haoyu |
| Workflow Automation | Nov 12 | Not Started | Haoyu |
| Exploratory Analysis | Nov 14 | Not Started | Bingqing |
| Statistical Modeling | Nov 17 | Not Started | Bingqing |
| Documentation | Nov 20 | Not Started | Both |
| Final Report | Nov 28 | Not Started | Both |

---

## Changes to Project Plan

Based on feedback received from our initial project plan, we clarified our data acquisition approach to explicitly use two different access methods - API-based retrieval for CPI and direct download for PCE. We enhanced our quality assessment procedures to include more comprehensive validation checks beyond basic missing value detection.

The overall project structure remains consistent with our original plan. All data acquisition and preparation tasks have been completed on schedule. No major deviations from the timeline have been necessary, and we remain on track to complete all remaining milestones by the final deadline.

---

## Challenges and Solutions

One challenge we encountered was ensuring reliable data retrieval from two different sources with different access methods. The FRED API required proper authentication handling, while the CSV download needed fallback mechanisms for reliability. We addressed this by implementing robust error handling and retry logic in both acquisition scripts.

We also needed to carefully handle timezone information in metadata to ensure accurate documentation of when data was retrieved. We resolved this by consistently using UTC timestamps throughout all metadata files, preventing any ambiguity across different computing environments.

---

## Individual Contributions

### Haoyu's Contributions

I completed all data acquisition, integration, enrichment, and quality assessment tasks for this milestone. I developed the code to retrieve CPI data from the FRED API and PCE data via CSV download, implementing proper error handling for both methods. I created the data integration script to merge the datasets and validated the merge results. I also developed the enrichment code to calculate the CPI index, real PCE, and all year-over-year growth rates.

Additionally, I implemented the quality assessment procedures and generated comprehensive metadata files for all datasets. I structured the project directory and documented all acquisition and processing steps. The time invested in these tasks totaled approximately 25 hours including development, testing, and documentation.

All completed work has been committed to our GitHub repository including the data acquisition notebook, all raw and processed data files, and accompanying metadata documentation.

### Bingqing's Contributions

I contributed to the overall project planning and actively participated in defining the research objectives and analytical framework. I reviewed the data acquisition and integration process developed by Haoyu to ensure consistency, completeness, and alignment with our research goals.

Currently, I am preparing for the exploratory data analysis (EDA) phase by identifying appropriate visualization techniques and statistical approaches for analyzing monthly time series data. This includes designing plots to highlight temporal trends, correlations, and potential lag effects between inflation and consumer spending.

In the upcoming weeks, I will lead the EDA and statistical modeling phases. My responsibilities will include conducting correlation and regression analyses to quantify the relationship between inflation (CPI growth) and real personal consumption expenditures (PCE), evaluating model performance, and interpreting the results within an economic context. I will also contribute to preparing the final report, integrating analytical findings with supporting visualizations and interpretations.

---

## Next Steps

Following the submission of this interim status report, our next priority will be completing the workflow automation task to ensure full reproducibility and transparency of the data pipeline. This step will include developing a Snakemake workflow that automates data acquisition, integration, enrichment, and quality assessment.

After workflow automation is finalized, Bingqing will lead the exploratory data analysis phase. This will involve generating time series visualizations, conducting correlation analysis, and summarizing key descriptive statistics to identify major patterns and trends. Insights from this analysis will guide the specification of our regression models.

Subsequently, we will proceed with the statistical modeling phase to formally evaluate the relationship between inflation and real consumer spending, including potential lagged effects. We will continue to adhere to our current project timeline and aim to complete all remaining tasks by the planned schedule.

