# Import statements
import streamlit
import requests
import snowflake.connector

import datetime
#use this for Control of Flow changes - error message handling
#from urllib.error import URLError

streamlit.title('Actions and Issues Tracker')

# -- connect to snowflake and populate the cursor
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# -- test the connection
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

# -- execute Snowflake query
my_cur.execute("SELECT * FROM tblTruckPayloadTargets")

#--my_data_row = my_cur.fetchone()
# -- Populate the dataframe
my_data_rows = my_cur.fetchall()
streamlit.header("Action/ Issue Register")
streamlit.dataframe(my_data_rows)



# -- new action variables
#action_date = streamlit.date_input('Action date:')                        
#streamlit.write('selected action date is:', action_date)
