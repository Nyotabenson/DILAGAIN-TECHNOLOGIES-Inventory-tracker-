import streamlit as st 
import pandas as pd 
import numpy as np 
import datetime


#page configuration
#st.set_page_config(page_title=page_title,page_icon=page_icon, layout=layout)


st.title("DILAGAIN TECHNOLOGIES")
st.header("Packaging Materials Inventory")

st.write("##")


#display dataset
df = pd.read_csv('dataset.csv')

st.write("Recent Entries")
st.write(df.tail(3))

#Sidebar
st.sidebar.header("DATA ENTRIES")
st.sidebar.subheader("INBOUND")
inbound = st.sidebar.checkbox("Expand Inbound")
if inbound:
    in_date = st.sidebar.date_input("Inbounding Date")

st.write('---')

#inbound list

st.sidebar.subheader("OUTBOUND")
DT = st.sidebar.date_input("DATE")
CT = st.sidebar.number_input("CLEAR TAPES", min_value=0, step=1)
KG50 = st.sidebar.number_input("50", min_value=0, step=1)
KH90 = st.sidebar.number_input("90", min_value=0, step=1)

if st.sidebar.button("Save"):
    df = pd.concat([df, pd.DataFrame({'Date' : DT, "Clear_tapes" : CT, "50kgs_sucks": KG50, "90kgs_sucks" : KH90}, index=[0])], ignore_index=True)
    df.to_csv("dataset.csv", index=False)

st.write(df)    