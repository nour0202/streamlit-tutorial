import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_excel(r"https://github.com/nour0202/streamlit-tutorial/blob/main/Data_set.csv")

st.set_page_config(page_title='Company Portfolio')
st.title('Company Portfolio 2023')
st.subheader('Welcome to XYZ Co!')

st.markdown('---')

#insert select box

selected_Segment = st.selectbox("Select a Segment", ['All'] + list(df['Segment'].unique()))

fil_df = df[df.Segment == selected_Segment]

fig = px.bar(
    fil_df if selected_Segment != 'All' else df,  # Use filtered data if applicable
    x="Segment",
    y="Profit",
    title="Profit Distribution by Customer Segment"
)

st.plotly_chart(fig) 

st.write("This pie chart the percentages of profit as of each segment.")
st.write("As shown in the figure, Consumer Segment accounts for the highest portion of profits which is approximately 45K.")

st.markdown("---") #horizontal line

#insert bar graph

fig = px.bar(
      df,
      x="Segment",
      y="Profit",
      title="Profit Per Customer Segment"       
)
fig

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
