import streamlit
import pandas as pd

# Title 
streamlit.title('My Parents New Healthy Diner')

# Header
streamlit.header('Breakfast Favorites')

# Breakfast favorites Items
streamlit.text('🫐 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')

# BYO Smoothie Header
streamlit.header('🍌 🍓 Build Your Own Fruit Smoothie')

# read in fruit list 
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


