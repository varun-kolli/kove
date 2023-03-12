import pandas as pd
import streamlit as st
from phase1 import introduction

tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

# Create a sidebar with buttons
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

# Create a sidebar with buttons for each tab
st.sidebar.markdown("# Tab Selector")
selection = [st.sidebar.button(tab, key=tab, help=tab, type='primary') for tab in tabs]

# Depending on which tab is selected, show the appropriate content
if selection[0]:
    st.header("Introduction")
    st.write("This is the introduction tab.")
if selection[1]:
    st.header("Initial Modelling")
    st.write("This is the initial modelling tab.")
if selection[2]:
    st.header("Decision Tree Improvements")
    st.write("This is the decision tree improvements tab.")
if selection[3]:
    st.header("Data Balancing")
    st.write("This is the data balancing tab.")
if selection[4]:
    st.header("Random Forest")
    st.write("This is the random forest tab.")