import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/refuress/app_test/main/weather_hourly_darksky.csv")

st.set_page_config(
   page_title = 'Real-Time Weather Hourly Dashboard',
   page_icon = '🔥',
   layout = 'wide'
)

st.title("Real-Time Weather Hourly Dashboard")

st.sidebar.subheader("Filter")

df


#summary = st.sidebar.multiselect(
#    "select the final type:",
#    options = df["summary"].unique(),
#    default = df["summary"].unique()
#)

#df_selection = df.query("summary == @summary")

#st.dataframe(df_selection)

