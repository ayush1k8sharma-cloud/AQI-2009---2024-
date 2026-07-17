# India AQI Analysis & Dashboard

A comprehensive data science project analyzing India's Air Quality Index (AQI) trends from 2009–2024, built as a CSE AI/ML college project at DAVIET, Jalandhar.

**Author:** Ayush Sharma | Roll No. 2513533 | CSE AI/ML, DAVIET

---

## Project Overview

This project analyzes air quality data across India using PM2.5 pollutant measurements, covering **483 monitoring stations**, **240 cities**, and **20 states**, from **2009 to 2024**. The project spans the full data science lifecycle — data loading, cleaning, AQI calculation, exploratory analysis, visualization, and an interactive Streamlit dashboard — with a dedicated spotlight on Punjab (home state) and Amritsar (station PB03).

## Dataset

- **Source:** Kaggle dataset by [omsandeeppatil]
- **Structure:** 546 CSV files organized across 20 state folders
- **Coverage:** 483 stations, 240 cities, 20 states, 2009–2024
- **Processing:** Raw CSVs are consolidated once via `prepare_data.py` into a single `processed_aqi.parquet` file for fast dashboard loading

## AQI Calculation Methodology

AQI is derived from PM2.5 concentration using piecewise linear interpolation, since PM2.5 shows a ~0.95 correlation with official AQI values in this dataset.

**Formula:**

```
Ip = ((IHi - ILo) / (BPHi - BPLo)) x (Cp - BPLo) + ILo
```

Two breakpoint standards were explored:

| Standard | Categories | Notes |
|---|---|---|
| **US EPA** | Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, Hazardous | Originally implemented in the pipeline |
| **CPCB (India)** | Good, Satisfactory, Moderate, Poor, Very Poor, Severe | More faithful to Indian air quality standards; recommended given the dataset is India-specific |

> Note: Official CPCB AQI takes the **maximum** sub-index across all measured pollutants (PM2.5, PM10, NO2, SO2, CO, O3, NH3, Pb), not just PM2.5. This project uses PM2.5 as a single-pollutant proxy due to dataset limitations.

## Analysis Phases

1. **Data Loading** — 546 CSV files ingested via `glob` and `pandas`
2. **Data Cleaning** — missing value handling, AQI calculation, feature engineering
3. **National AQI Trend Analysis** — 2009–2024 trend
4. **State & City Analysis**
5. **Station Deep Dive**
6. **Seasonal Pattern Analysis**
7. **Pollutant Analysis**
8. **AQI Category Distribution**

## Tech Stack

- **Data processing:** Python, pandas, glob
- **Visualization:** matplotlib, seaborn, plotly
- **Dashboard:** Streamlit
- **Presentation:** PowerPoint (python-pptx) — `India_AQI_Analysis.pptx` (13 slides)

## Dashboard Structure

A centralized `theme.py` module provides shared theming and utilities across all pages:
`get_theme()`, `inject_theme_css()`, `get_chart_layout()`, `render_sidebar()`, `render_footer()`, `bar_color_from_aqi()`, `aqi_bucket_color()`, `MONTHS`, `BUCKET_ORDER`

**Pages:**

| File | Description |
|---|---|
| `Home.py` | Landing page |
| `01_National_Trend.py` | National AQI trend over time |
| `02_State_City.py` | State and city-level comparisons |
| `03_Station_Analysis.py` | Individual station deep dive |
| `04_Seasonal_Patterns.py` | Seasonal AQI patterns |
| `05_Pollutant_Analysis.py` | Pollutant-level breakdown |
| `06_Punjab_Spotlight.py` | Punjab-focused analysis: stubble burning seasonality, station rankings vs. national average |
| `07_AQI_Categories.py` | AQI category distribution |
| `08_FAQ.py` | Project FAQ |

### Development Notes

- **Chart layout rule:** `xaxis`/`yaxis` must **never** be included inside the `CHART_LAYOUT` dict. Always call `fig.update_xaxes()` / `fig.update_yaxes()` separately *after* `fig.update_layout(**CL, ...)` to avoid a "multiple values for keyword argument" error.
- **Correct page structure order:**
  ```
  imports → set_page_config() → get_theme() → inject_theme_css()
  → get_chart_layout() → render_sidebar() → load data → page content
  ```

## Planned ML Extension

A machine learning component is planned to extend the project from analysis into prediction:

- **Objective options:** AQI category classification, AQI/PM2.5 regression, or short-term forecasting
- **Feature engineering:** lag features (1/3/7-day), rolling means/std, calendar features (month, day-of-week, stubble-burning season flag), cyclical encoding
- **Candidate models:** Random Forest / XGBoost / LightGBM (tabular baseline), SARIMA / Prophet (time-series, e.g. for Punjab Spotlight), LSTM (optional deep learning angle)
- **Evaluation:** Accuracy/F1 (classification) or RMSE/MAE/MAPE (regression), benchmarked against a naive baseline
- **Dashboard integration:** Planned `09_AQI_Prediction.py` page using a `joblib`-serialized model

## Project Structure

```
project/
├── prepare_data.py          # One-time raw CSV → parquet processing
├── processed_aqi.parquet    # Cleaned, consolidated dataset
├── theme.py                 # Shared dashboard theming/utilities
├── Home.py                  # Dashboard entry point
├── pages/
│   ├── 01_National_Trend.py
│   ├── 02_State_City.py
│   ├── 03_Station_Analysis.py
│   ├── 04_Seasonal_Patterns.py
│   ├── 05_Pollutant_Analysis.py
│   ├── 06_Punjab_Spotlight.py
│   ├── 07_AQI_Categories.py
│   └── 08_FAQ.py
├── India_AQI_Analysis.pptx  # Project presentation (13 slides)
└── README.md
```

## Running the Dashboard

```bash
pip install pandas streamlit plotly seaborn matplotlib
streamlit run Home.py
```

---
