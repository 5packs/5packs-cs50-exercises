import streamlit as st
from streamlit_folium import st_folium
import folium
import requests


st.sidebar.markdown("# Home")

st.title("GPoznanS")

content = """
This website will help you in navigating throught the depths of the city of Poznan in a more comfortable manner
"""

st.write(content)

m = folium.Map(location=[52.406786, 16.930360], zoom_start=12)
st_data = st_folium(m, width = 725, height=400)

copyright = """
A significant part of the content and data presented in the system of the Poznań
Internet Plan in the form of information and services can be automatically 
downloaded and reused as public data. The condition for their use is the indication 
of the source of origin (Miasto Poznań, the website poznan.pl). 
Spatial data is published in GeoJSON, GeoRSS, KML, GML formats.

Access to this data is via the platform http://egov.psnc.pl/node/29
"""
st.text(copyright)

