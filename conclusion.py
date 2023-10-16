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

def page_conclusion():
    #Last part, the conclusion:
    st.header('IV. Conclusion')
    st.write("In conclusion, the study of instantaneous fuel prices in France reflects a complex and fluctuating dynamic, strongly influenced by various economic, geopolitical and environmental factors. The observation that prices tend to fall thanks to the actions of large retailers selling at cost price is interesting, because it shows that competition in the fuel market can have positive repercussions on consumers' wallets.")
    st.write("However, it is crucial to note that this downward price trend may be fleeting, and that several external factors can reverse this trend. Geopolitical conflicts, such as the Ukraine-Russia war and the Israel-Palestine conflict, have traditionally impacted global oil markets by causing sharp fluctuations in oil prices. Volatility in fuel prices due to these events may negate the temporary benefits of large retailers selling at cost.")
    st.write("In addition, the current context is marked by a government trend towards the promotion of electric vehicles and alternative energies, with the aim of reducing dependence on fossil fuels and combating climate change. This policy could potentially result in taxes or regulations aimed at discouraging the use of gasoline or diesel vehicles, which could ultimately increase costs for motorists.")
    st.write("Ultimately, the study of instantaneous fuel prices in France highlights the need for consumers to remain attentive to market fluctuations, while considering more sustainable alternatives, such as the adoption of electric vehicles, to deal with uncertainties related to fuel prices and geopolitical issues. Government policies and the actions of large retailers can play a role, but diversifying means of transport and reducing dependence on fossil fuels are crucial challenges to address in a constantly changing global context.")
    st.image('https://images.datacamp.com/image/upload/v1640050215/image27_frqkzv.png', width=700)