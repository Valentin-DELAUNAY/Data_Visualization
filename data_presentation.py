#Importation of the libraries:
import pandas as pd
import numpy as np
import missingno as msno
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
import folium
from folium.plugins import HeatMap
import plotly.express as px
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
import json

def page_data_presentation(instant_fuel):
    st.header('II. Short presentation of data')
    presentation_selection=st.selectbox('Select the type of information you need:', ['The name of the columns', 'The first 20 lines', 'The name of the columns with their type', 'The desciption of the dataset', 'The shape of the dataset', 'The number of missing values and the number of duplicates'])
    if (presentation_selection=='The name of the columns'):
        st.write('The dataset contains the following columns:')
        column_names = instant_fuel.columns.tolist()
        half_length = len(column_names) // 2
        column_names_left = column_names[:half_length]
        column_names_right = column_names[half_length:]
        left_table = pd.DataFrame({'Column Name': column_names_left}).to_markdown(index=False)
        right_table = pd.DataFrame({'Column Name': column_names_right}).to_markdown(index=False)
        columns = st.columns(2)
        with columns[0]:
            st.markdown(left_table)
        with columns[1]:
            st.markdown(right_table)
        st.write(' ')
        st.write('The dataset have ' + str(instant_fuel.shape[0]) + ' lines and ' + str(instant_fuel.shape[1]) +' columns in total.')
    elif (presentation_selection=='The first 20 lines'):
        st.write('The first 20 lines of the dataset are:')
        st.write(instant_fuel.head(20))
    elif (presentation_selection=='The name of the columns with their type'):
        st.write('The dataset contains the following columns with their type:')
        column_info = instant_fuel.dtypes
        num_columns = len(column_info)
        third_length = num_columns // 3
        column_info_part1 = column_info.iloc[:third_length]
        column_info_part2 = column_info.iloc[third_length:2 * third_length]
        column_info_part3 = column_info.iloc[2 * third_length:]
        column_info_df_part1 = pd.DataFrame({'Column Name': column_info_part1.index, 'Data Type': column_info_part1.values})
        column_info_df_part2 = pd.DataFrame({'Column Name': column_info_part2.index, 'Data Type': column_info_part2.values})
        column_info_df_part3 = pd.DataFrame({'Column Name': column_info_part3.index, 'Data Type': column_info_part3.values})
        columns = st.columns(3)
        columns[0].dataframe(column_info_df_part1.set_index('Column Name'))
        columns[1].dataframe(column_info_df_part2.set_index('Column Name'))
        columns[2].dataframe(column_info_df_part3.set_index('Column Name'))
        st.write('The dataset have ' + str(instant_fuel.shape[0]) + ' lines and ' + str(instant_fuel.shape[1]) +' columns in total.')
    elif (presentation_selection=='The desciption of the dataset'):
        st.write('Some information about the dataset:')
        st.write(instant_fuel.describe())
        st.write('The dataset have ' + str(instant_fuel.shape[1]) +' columns in total.')
    elif (presentation_selection=='The shape of the dataset'):
        st.write('The dataset have ' + str(instant_fuel.shape[0]) +' rows and ' + str(instant_fuel.shape[1]) +' columns in total.')
    elif (presentation_selection=='The number of missing values and the number of duplicates'):
        st.write('The number of missing values in the dataset is:')
        st.bar_chart(instant_fuel.isnull().sum())
        st.write('There is ' + str(instant_fuel.duplicated().sum()) + ' values duplicated in the dataset.')