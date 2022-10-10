import streamlit

streamlit.title('My parents new healthy dinner ')
streamlit.header('Breakfast menu    ')
streamlit.text('🥗 Omega 3 & blueberry oatmeal')
streamlit.text('🥣 Kale, spinach & rocket Smoothie')
streamlit.text('🐔 Hard boiled free-Range Egg')
streamlit.text('🥑🍞 Avacaddo toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','strawberries'])

# fruits_to_show=my_fruit_list.loc[fruits_selected]
# streamlit.dataframe(fruits_to_show)
# streamlit.dataframe(fruits_to_show)


