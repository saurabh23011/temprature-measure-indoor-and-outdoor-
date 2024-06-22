import streamlit as st
import requests

# Set up your API key for OpenWeatherMap
API_KEY = 'e7816266b7fb1b25d3126f54fbc2b91a'
CITY = 'Delhi'

# Function to get outdoor temperature
def get_outdoor_temperature():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['main']['temp']
    else:
        st.error("Failed to get outdoor temperature")
        return None


def get_indoor_temperature():

    return 22.5

# Streamlit app
st.title('Indoor and Outdoor Temperature Monitor')

# Display outdoor temperature
outdoor_temp = get_outdoor_temperature()
if outdoor_temp is not None:
    st.write(f"Outdoor Temperature: {outdoor_temp} °C")

# Display indoor temperature
indoor_temp = get_indoor_temperature()
if indoor_temp is not None:
    st.write(f"Indoor Temperature: {indoor_temp:.2f} °C")
