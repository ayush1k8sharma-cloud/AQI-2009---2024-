import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_all_data():
    parquet_path = "processed_aqi.parquet"
    if os.path.exists(parquet_path):
        df = pd.read_parquet(parquet_path)
        pollutants = [p for p in ['pm2.5','pm10','no2','so2','co','ozone','nh3'] if p in df.columns]
        stations = pd.read_csv("stations.csv")
        return df, stations, pollutants
    else:
        st.error("⚠️ processed_aqi.parquet not found! Run prepare_data.py first.")
        st.code("python prepare_data.py")
        st.stop()