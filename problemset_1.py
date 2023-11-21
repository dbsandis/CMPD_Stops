# Import packages

import pandas as pd
import altair as alt
import streamlit as st


# Load traffic stops data and create a dataframe called stops
# and check the columns and their types
# Officer_Traffic_Stops.csv

Stops_File = 'Officer_Traffic_Stops.csv'

# Upload a CSV file

stops = pd.read_csv(Stops_File)

st.write("DataFrame from CSV Data Types:")
st.write(stops.dtypes)

# view the data by just typing the dataframe name

st.write('View Data frame')
st.dataframe(stops)

# check the data using df.info()
st.write('View DataFrame Info')
st.table(stops.describe())

## Bar chart
st.write('Bar Chart of Was_a_Search_Conducted')


# Use the selected columns for the bar chart
st.bar_chart(stops, category='Month_of_Stop',  value='Was_a_Search_Conducted')





