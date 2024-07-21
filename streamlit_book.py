import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv("https://raw.githubusercontent.com/nour0202/streamlit-tutorial/main/Data_set.csv", encoding='ISO-8859-1')

st.set_page_config(page_title='Company Portfolio')
st.title('Company Portfolio 2023')
st.subheader('Welcome to XYZ Co!')

st.markdown('---')

#insert select box

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

option = st.selectbox(
        "Select a Segment",
        ("All", "Consumer", "Home Office Segment", "Corporate"),
        key=df,
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
)

#insert bar graph

fig = px.bar(
      df,
      x="Segment",
      y="Profit",
      title="Profit Per Customer Segment"       
)
fig 

st.markdown("---") #horizontal line

st.write("This bar chart shows the total sales for each state within the specified range. You can scroll the slide bar and specify the minimum and the maximum amount of sales.")
st.write("By hovering on the columns, California registered the highest sales, then New York, and then Washington having 146K, 93k, 65k, respectively.")

st.markdown("---")

#insert bar graph

fig = px.histogram(
    df,
    x="State",
    y="Sales",
    title="Sales Across the States"
)
fig

st.write("This bar chart shows the total sales for each state within the specified range. You can scroll the slide bar and specify the minimum and the maximum amount of sales.")
st.write("By hovering on the columns, California registered the highest sales, then New York, and then Washington having 146K, 93k, 65k, respectively.")

st.markdown("---")

#insert check box

agree = st.checkbox('I am not a Robot')

if agree:
    st.write('Welcome!')
