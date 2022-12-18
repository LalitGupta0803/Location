import streamlit as st
import requests
st.write("Welcome To Project X")
url = "https://maps.googleapis.com/maps/api/distancematrix/json"
def apiCall(myData):
    headers = {"origins":"{}".format(myData[0]),
    "destinations":"{}".format(myData[1]),
    "key":"{}".format(myData[2])}
    data = requests.get(url,params=headers)
    st.write(data.json())
def getUserData():
    origin = st.text_input("Enter Your Current Location")
    destination = st.text_input("Enter Your Destination")
    key = st.text_input("Enter Key Here")
    if st.button("Click Me"):
        apiCall([origin,destination,key])
getUserData()