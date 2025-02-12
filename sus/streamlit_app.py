import streamlit as st
import requests

st.title("Energy Optimization App")

def get_example():
    response = requests.get("http://localhost:5000/api/example")
    if response.status_code == 200:
        return response.json()
    else:
        return {"message": "Error"}

example_data = get_example()
st.write(example_data)