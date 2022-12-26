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

#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()

streamlit.header("Action/ Issue Register")
#streamlit.dataframe(my_data_row)
#streamlit.dataframe(my_data_rows)

# new action variables
action_date = streamlit.text_input('Action date:')

# ----------Testing---------------
df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df, 200, 100)
# --------------------------------
