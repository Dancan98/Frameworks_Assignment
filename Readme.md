# CORD-19 Metadata Exploration Project

## Overview
This project explores the `metadata.csv` file from the CORD-19 dataset. The goal is to clean, analyze, and visualize patterns in COVID-19 related research publications.

---

## Key Tasks Completed

### ✅ Data Loading & Cleaning
- Loaded and explored the CORD-19 metadata.csv
- Handled missing values (dropped or filled as appropriate)
- Converted dates and extracted publication year
- Created derived columns such as abstract word count

### ✅ Data Analysis
- Counted publications by year
- Identified top journals by volume
- Analyzed most frequent words in paper titles

### ✅ Visualizations
- Bar chart of papers per year
- Bar chart of top journals
- Word cloud of paper titles

### ✅ Streamlit App
- Interactive filters (year range)
- Live charts and data table
- Word cloud generation

---

## Key Findings

- **Publication Spike**: A sharp increase in research output was observed in 2020.
- **Preprint Servers**: Journals like *medRxiv* and *bioRxiv* were among the top sources.
- **Common Title Keywords**: "COVID-19", "SARS-CoV-2", and "pandemic" were frequent.

---

## Challenges Faced

- Some rows had missing or invalid dates.
- The dataset was large, requiring efficient filtering and caching.
- Streamlit plotting required integration with matplotlib.

---

## What I Learned

- Importance of handling missing data early.
- Efficiently creating visual summaries of large datasets.
- Building user-friendly Streamlit apps for data exploration.

---

## How to Run

### Prerequisites

- Python 3.x
- Install required packages:
```bash
pip install pandas matplotlib seaborn wordcloud streamlit
