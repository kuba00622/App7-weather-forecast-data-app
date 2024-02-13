import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('happy.csv')

st.title('In Search for Happiness')
x_axis = st.selectbox('Select the data for the X-axis', ('happiness', 'gdp', 'social_support'))
y_axis = st.selectbox('Select the data for the y-axis', ('happiness', 'gdp', 'social_support'))
match x_axis:
    case 'happiness':
        x = df['happiness']
    case 'gdp':
        x = df['gdp']
    case 'social_support':
        x = df['social_support']

match y_axis:
    case 'happiness':
        y = df['happiness']
    case 'gdp':
        y = df['gdp']
    case 'social_support':
        y = df['social_support']


st.header(f'{x_axis} and {y_axis}')
figure = px.line(x=x, y=y, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)
