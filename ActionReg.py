# Import statements
import streamlit
import requests
import snowflake.connector
#use this for Control of Flow changes - error message handling
#from urllib.error import URLError

streamlit.title('Actions and Issues Tracker')

#streamlit.header('Breakfast Menu')
#streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

#test snowflake connection
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT Truckclass FROM tblTruckPayloadTargets")
my_data_row = my_cur.fetchone()
streamlit.header("test data")
streamlit.dataframe(my_data_row)
