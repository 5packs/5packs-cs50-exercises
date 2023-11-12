import streamlit as st
from streamlit_folium import st_folium
import folium
import requests


st.sidebar.markdown("# Parking Ticket Machines")

st.title("Parking Ticket Machines")

# ----------------- Parking Tickets -----------------
parkingapi = requests.get("https://www.poznan.pl/mim/plan/map_service.html?mtype=pub_transport&co=parking_meters").json()
parkingAutomat = parkingapi["features"]

m = folium.Map(location=[52.402774, 16.917845], zoom_start=14)

for parking in parkingAutomat:
    coordinatesFlipped = parking["geometry"]["coordinates"]
    coordinates = [coordinatesFlipped[1], coordinatesFlipped[0]]
    properties = parking["properties"]
    name = f"{properties['street']}-{properties['zone']}"
    payment = f"Coins:{properties['bilon']}\nBLIK:{properties['blik']}\nCard:{properties['karta']}\nPEKA:{properties['peka']}"
    folium.Marker(
        coordinates,
        popup=f"{name}\n{payment}",
        tooltip=name
    ).add_to(m)

st_data = st_folium(m, width=725)
