# Project Plan: The Impact of Inflation on U.S. Consumer Spending (2015–2024)

## Overview
The overall goal of this project is to analyze how inflation has influenced consumer spending behavior in the United States between 2015 and 2024. Over the past decade, and especially since 2020, inflation levels have fluctuated significantly due to factors such as the COVID-19 pandemic, supply chain disruptions, and changing fiscal and monetary policies. This project aims to examine whether rising inflation corresponds to a reduction in real consumer spending, which reflects changes in purchasing power.  

Through this project, we will apply a full data lifecycle approach that includes data collection, integration, cleaning, quality assessment, and documentation. The analysis will be conducted using reproducible workflows in Python, following ethical data handling practices and transparency standards. Our findings may help policymakers and businesses understand how inflation impacts household consumption patterns and economic stability.

---

## Research Questions
This project seeks to address the following research questions:  
1. How has rising inflation since 2020 affected real consumer spending in the United States?  
2. What is the statistical relationship between inflation (as measured by the Consumer Price Index) and total personal consumption expenditures?  
3. Does the effect of inflation on spending appear immediately, or does it occur with a time lag?  

These questions will guide our data analysis and modeling process. We will use time series data to explore both short-term and long-term relationships between inflation and real spending. The analysis will help identify whether inflation significantly constrains consumers’ ability to spend over time.

---

## Team
This project will be completed by a team of two members: Bingqing and Haoyu. Both members will actively collaborate throughout all stages of the project while maintaining clear divisions of responsibility to ensure efficiency and accountability.

Haoyu will focus on data acquisition, integration, and storage. This includes obtaining the Consumer Price Index (CPI) and Personal Consumption Expenditures (PCE) datasets from the Federal Reserve Economic Data (FRED) database, cleaning and organizing them, and preparing the merged dataset for analysis.  

Bingqing will take primary responsibility for data analysis, visualization, and documentation. This includes performing exploratory data analysis, generating time series plots, building regression models, and interpreting results. Both members will jointly contribute to writing the project documentation and ensuring that all steps are clearly recorded for reproducibility.

---

## Datasets
To answer our research questions, we will use two key datasets from the FRED platform.  

The first dataset is the Consumer Price Index, published by the U.S. Bureau of Labor Statistics (BLS). This dataset measures the average change over time in the prices paid by urban consumers for a basket of goods and services. It is one of the most widely used indicators of inflation and reflects overall changes in cost of living.  

The second dataset is the Personal Consumption Expenditures dataset, published by the U.S. Bureau of Economic Analysis (BEA). PCE measures the total value of goods and services purchased by U.S. consumers and serves as a primary indicator of consumer spending. 

Both datasets are publicly available, updated monthly, and can be retrieved programmatically using an API key from the FRED database. They are reliable, well-documented, and suitable for academic use without licensing concerns. The data will be stored systematically in a structured folder within our GitHub repository, ensuring transparency and reproducibility.

---

## Timeline

### Data acquisition 
Haoyu will obtain the CPI and PCE datasets from the FRED database using the FRED API. Haoyu will record metadata such as series IDs, data frequency, and retrieval date to ensure data traceability. Data integrity will be verified using file checksums to confirm that the downloaded files have not been altered. These steps are expected to be completed around **October 20th**.

### Storage and Organization
Haoyu will organize the project folder structure to maintain consistency and reproducibility. This will include creating directories such as data/raw, data/processed, scripts, and docs for efficient data management. The raw datasets will be loaded into Python for inspection and stored systematically with clear, descriptive file names. This step is expected to be completed around **October 25th**.

### Extraction and Enrichment
Haoyu will extract key variables and create new analytical features to enhance the dataset. These include computing real PCE (inflation-adjusted spending), indexing values to the 2015 base year, and calculating both monthly and yearly growth rates. All derived variables will be defined and documented in the project’s data dictionary. This step is expected to be completed around **October 27th**.

### Data Integration
Haoyu will integrate the CPI and PCE datasets into a single unified dataset named macro_monthly.csv. The integration process will align both datasets by date and ensure consistent formatting, covering the entire period from 2015 to 2024. This integrated dataset will form the foundation for subsequent analysis. This stage is expected to be completed around **October 29th**.

### Data Quality and Cleaning
Haoyu will assess the quality of the integrated dataset by checking for missing data, duplicates, and inconsistencies. Any detected issues will be corrected or documented, and the overall data reliability will be summarized in a brief quality report. This step is expected to be completed around **November 1st**.

### Workflow Automation
Haoyu will develop a Python script that automates the data collection, cleaning, and integration processes. The workflow will be tested to ensure that it can reproduce the final dataset directly from the raw files. This stage is expected to be completed around **November 10th**.

### Exploratory Data Analysis
Bingqing will perform exploratory data analysis to visualize and summarize patterns in the inflation and consumer spending data. The analysis will include time series plots, descriptive statistics, and correlation analysis to reveal initial insights. This step is expected to be completed around **November 12th**.

### Modeling and Statistical Analysis
Bingqing will conduct statistical modeling to analyze how inflation affects real consumer spending over time. This will include building regression and lag models, interpreting results, and visualizing model outcomes. This task is expected to be completed around **November 17th**.

### Workflow Documentation and Metadata
Haoyu and Bingqing will jointly document the full workflow, including metadata for each dataset, variable definitions, and a description of all processing steps. A data dictionary and workflow summary will be prepared to ensure full transparency and reproducibility. This stage is expected to be completed around **November 19th**.

### Metadata and Data Documentation
Haoyu and Bingqing will create comprehensive metadata and documentation for the final dataset. This will include a data dictionary or codebook (as a text or PDF file) describing all variables, sources, and transformations. Additionally, a descriptive metadata file will be created in accordance with the DataCite or Schema.org standard, providing project-level information such as title, contributors, version, keywords, and temporal coverage. This work is expected to be completed around **November 20th**.

### Final Report and Submission
Haoyu and Bingqing will compile the final report that includes the project methodology, analysis results, and conclusions. All scripts, data files, and outputs will be uploaded to Box, and access permissions will be verified before submission. The final project materials are expected to be completed and submitted around **November 28nd**.

---

## Constraints
There are several known constraints that may affect our project. Time is the most significant limitation, as the semester schedule restricts the depth of analysis we can perform. Data availability is another potential constraint, as FRED datasets are sometimes updated with a short delay. Additionally, the project focuses only on national-level data, meaning regional variations or demographic-specific spending behaviors will not be captured. 

A further limitation involves the use of SQL for data management and analysis. While SQL is effective for storing, querying, and integrating datasets, it offers limited support for advanced statistical modeling and visualization. Regression analysis, correlation testing, and time-series modeling require mathematical libraries and visualization tools that SQL alone cannot provide. Therefore, the project will rely primarily on Python for analytical tasks, while SQL (if used) will be limited to data organization or preliminary queries.

---

## Gaps and Areas Needing Input
There are a few areas where we may need additional guidance or input. First, we plan to seek feedback on the most appropriate regression model to capture the relationship between inflation and consumer spending—whether a simple linear model or a lagged time-series approach would be more appropriate. Second, we will confirm FRED’s official data licensing terms, although educational use is generally permitted. Additionally, if SQL is used during the data preparation stage, we would appreciate guidance on best practices for managing and querying data efficiently. Because SQL joins can be complex when handling time series datasets, improper joins or mismatched date keys may generate duplicate or inconsistent records that could negatively affect the accuracy of our analysis. We seek advice on how to structure queries and design table relationships to maintain data integrity and minimize redundancy before importing data into Python for analysis.

We may also need advice on implementing workflow automation in Python to ensure that our project can be fully reproduced. Finally, we will seek feedback on the best practices for documenting metadata and ensuring compliance with course reproducibility standards.

---


