# Import statements
import streamlit
import requests
import snowflake.connector

# ----------Testing---------------
import pandas as pd
import numpy as np

# --------------------------------
#use this for Control of Flow changes - error message handling
#from urllib.error import URLError

streamlit.title('Actions and Issues Tracker')

#test snowflake connection
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM tblTruckPayloadTargets")


streamlit.header("Action/ Issue Register")
#streamlit.dataframe(my_data_row)
#streamlit.dataframe(my_data_rows)

# new action variables
action_date = streamlit.text_input('Action date:')

# ----------Testing----------------------------------------------------------------------------------------------------
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

# ----------Testing----------------------------------------------------------------------------------------------------
