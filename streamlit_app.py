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
my_fruit_list = my_fruit_list.set_index('Fruit')

# fruits selected list
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on page
streamlit.dataframe(fruits_to_show)


