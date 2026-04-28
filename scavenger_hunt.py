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

