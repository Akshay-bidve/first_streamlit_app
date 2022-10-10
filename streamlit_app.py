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

streamlit.dataframe(my_fruit_list)
