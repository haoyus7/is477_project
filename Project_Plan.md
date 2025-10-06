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

Both datasets are publicly available, updated monthly, and accessible in CSV format from FRED. They are reliable, well-documented, and suitable for academic use without licensing concerns. The data will be stored systematically in a structured folder within our GitHub repository, ensuring transparency and reproducibility.

---

## Timeline






---

## Constraints
There are several known constraints that may affect our project. Time is the most significant limitation, as the semester schedule restricts the depth of analysis we can perform. Data availability is another potential constraint, as FRED datasets are sometimes updated with a short delay. Additionally, the project focuses only on national-level data, meaning regional variations or demographic-specific spending behaviors will not be captured.  


---

## Gaps and Areas Needing Input
There are a few areas where we may need additional guidance or input. First, we plan to seek feedback on the most appropriate regression model to capture the relationship between inflation and consumer spending—whether a simple linear model or a lagged time-series approach would be more appropriate. Second, we will confirm FRED’s official data licensing terms, although educational use is generally permitted.  

We may also need advice on implementing workflow automation in Python to ensure that our project can be fully reproduced. Finally, we will seek feedback on the best practices for documenting metadata and ensuring compliance with course reproducibility standards.

---


