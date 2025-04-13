#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm  # colormap
from sympy import symbols, diff
from math import log

# Creating a title with streamlit. 
st.title("DataFest Python Notebook for Team Nuvon")
st.code(
    '''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm  # colormap
from sympy import symbols, diff
from math import log
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
    ''',
    language="python",
)
st.markdown("### Load Data and Preview ")

st.code(
    '''
leases = pd.read_csv("Leases.csv")
st.subheader("Leases Data Preview")
st.dataframe(leases.head())
    ''',
    language="python",
)
leases = pd.read_csv("Leases.csv")
st.subheader("Leases Data Preview")
st.dataframe(leases.head())
st.code(
    '''
occupancy = pd.read_csv("Major Market Occupancy Data-revised.csv")
st.subheader("Occupancy Data Preview")
st.dataframe(occupancy.head())
    ''',
    language="python",
)
occupancy = pd.read_csv("Major Market Occupancy Data-revised.csv")
st.subheader("Occupancy Data Preview")
st.dataframe(occupancy.head())
st.code(
    '''
price_availability = pd.read_csv("Price and Availability Data.csv")
st.subheader("Price and Availability Data Preview")
st.dataframe(price_availability.head())
    ''',
    language="python",
)
price_availability = pd.read_csv("Price and Availability Data.csv")
st.subheader("Price and Availability Data Preview")
st.dataframe(price_availability.head())
st.code(
    '''
unemployment = pd.read_csv("Unemployment.csv")
st.subheader("Unemployment Data Preview")
st.dataframe(unemployment.head())
    ''',
    language="python",
)
unemployment = pd.read_csv("Unemployment.csv")
st.subheader("Unemployment Data Preview")
st.dataframe(unemployment.head())

# -- Merge Data --
# Load datasets again
st.markdown("### Merging Data")
st.code(
    '''
leases = pd.read_csv("Leases.csv")
occupancy = pd.read_csv("Major Market Occupancy Data-revised.csv")
availability = pd.read_csv("Price and Availability Data.csv")
unemployment = pd.read_csv("Unemployment.csv")

# Standardize column names to lowercase
for df in [leases, occupancy, availability, unemployment]:
    df.columns = df.columns.str.lower()

final_data_ccdm_ready = leases.merge(
    availability, on=['year', 'quarter', 'market'], suffixes=('_lease', '_avail')
)
final_data_ccdm_ready = final_data_ccdm_ready.merge(
    occupancy[['year', 'quarter', 'market', 'avg_occupancy_proportion']],
    on=['year', 'quarter', 'market']
)
final_data_ccdm_ready = final_data_ccdm_ready.merge(
    unemployment[['year', 'quarter', 'state', 'unemployment_rate']],
    on=['year', 'quarter', 'state']
)

final_data_ccdm_ready.to_csv("final_data_ccdm_ready.csv", index=False)
st.subheader("Final Merged Dataset")
st.dataframe(final_data_ccdm_ready.head())
st.write("✅ Final merged dataset saved as 'final_data_ccdm_ready.csv'")
    ''',
    language="python",
)
leases = pd.read_csv("Leases.csv")
occupancy = pd.read_csv("Major Market Occupancy Data-revised.csv")
availability = pd.read_csv("Price and Availability Data.csv")
unemployment = pd.read_csv("Unemployment.csv")

# Standardize column names to lowercase
for df in [leases, occupancy, availability, unemployment]:
    df.columns = df.columns.str.lower()

final_data_ccdm_ready = leases.merge(
    availability, on=['year', 'quarter', 'market'], suffixes=('_lease', '_avail')
)
final_data_ccdm_ready = final_data_ccdm_ready.merge(
    occupancy[['year', 'quarter', 'market', 'avg_occupancy_proportion']],
    on=['year', 'quarter', 'market']
)
final_data_ccdm_ready = final_data_ccdm_ready.merge(
    unemployment[['year', 'quarter', 'state', 'unemployment_rate']],
    on=['year', 'quarter', 'state']
)

final_data_ccdm_ready.to_csv("final_data_ccdm_ready.csv", index=False)

st.subheader("Final Merged Dataset")
st.dataframe(final_data_ccdm_ready.head())
st.write("✅ Final merged dataset saved as 'final_data_ccdm_ready.csv'")

st.markdown("### Review Collapsed Data")
st.code(
    '''
ccdm = pd.read_csv("ccdm_collapsed_data.csv")
st.subheader("Collapsed Symbolic Manifold Data Preview")
st.dataframe(ccdm.head())
    ''',
    language="python",
)

ccdm = pd.read_csv("ccdm_collapsed_data.csv")
st.subheader("Collapsed Symbolic Manifold Data Preview")
st.dataframe(ccdm.head())

# --- An attempt to make website more dashboardy ---
# YOU CAN DELETE EVERYTHING BELOW THIS 
# Sidebar: add a filter for Year based on the merged data
years = final_data_ccdm_ready['year'].unique()
selected_year = st.sidebar.selectbox("Select Year", sorted(years))
st.sidebar.markdown("## Filtered Metrics")

# Calculate some metrics
st.sidebar.metric("filler filler", "100%")

st.sidebar.markdown("## filler chart")

fig2, ax2 = plt.subplots()
ax2.bar("filler", "filler")
ax2.set_xlabel("filler")
ax2.set_ylabel("filler filler")
ax2.set_title("filler filler filler filler")
st.sidebar.pyplot(fig2)
