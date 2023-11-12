import streamlit as st
from streamlit_folium import st_folium
import folium
import requests


st.sidebar.markdown("# Monuments")

st.title("Monuments in Poznan")
# -------------------- Monuments --------------------
monumentapi = requests.get("https://www.poznan.pl/mim/plan/map_service.html?mtype=pub_transport&co=class_objects&class_id=2572").json()
monuments = monumentapi["features"]

m = folium.Map(location=[52.408766, 16.934829], zoom_start=14)

for monument in monuments:
    coordinatesFlipped = monument["geometry"]["coordinates"]
    coordinates = [coordinatesFlipped[1], coordinatesFlipped[0]]
    properties = monument["properties"]
    name = f"{properties['nazwa']}"
    other = f"Address:{properties['adres']}\nDescription:{properties['opis']}"
    folium.Marker(
        coordinates,
        popup=f"{name}\n{other}",
        tooltip=name
    ).add_to(m)

st_data = st_folium(m, width=725)