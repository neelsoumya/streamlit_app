# Import packages
import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# write text
st.write("Wuhan Outbreak detective")

# sidebar
st.sidebar.header("Settings")
total_cases = st.sidebar.slider("Total cases", 100, 1000, 500)
cluster_pct =  st.sidebar.slider("Percentage of cases near source", 10, 90, 70)
show_source = st.sidebar.checkbox("Reveal true source")

# create synthetic data
market_lat, market_lon = 30.6195, 114.2577

cluster_count = int( total_cases * cluster_pct /100)
noise_count = total_cases - cluster_count

cluster_lats = np.random.normal(market_lat, 0.005, cluster_count)
cluster_lons = np.random.normal(market_lon, 0.005, cluster_count)

noise_lats = np.random.uniform(30.5, 30.7, noise_count)
noise_lons = np.random.uniform(114.2, 114.4, noise_count)

cases = pd.DataFrame({
  'lat': np.concatenate([cluster_lats, noise_lats]),
  'lon': np.concatenate([cluster_lons, noise_lons)
})




                               

