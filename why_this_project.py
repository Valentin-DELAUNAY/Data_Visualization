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

def page_why_project():
    #Presentation of the project (introduction):
    st.header('I. Why this project ?')
    st.write('In the current context, the "Fuel prices in France - Instant flow dataset" holds significant relevance due to the global challenges surrounding energy consumption, environmental sustainability, and economic stability.')
    st.write('With increasing fuel demand, particularly in the transportation sector, tracking and analyzing fuel prices in France is crucial. It provides essential insights into the economic impact of rising fuel costs on consumers, businesses, and the overall economy.')
    st.write('Furthermore, as countries seek to transition towards cleaner and more sustainable energy sources, understanding the fluctuations in fuel prices can inform policies aimed at reducing carbon emissions and promoting alternative energy solutions. The dataset is updated daily and contains information on fuel prices in France.')
    st.write('Lien pour accéder au jeu de données: https://www.data.gouv.fr/fr/datasets/prix-des-carburants-en-france-flux-instantane/')