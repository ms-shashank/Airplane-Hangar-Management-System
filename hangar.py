# import streamlit as st
# import sqlite3
# import pandas as pd

# # Connect to SQLite database
# conn = sqlite3.connect('hangar.db')

# # Title of the app
# st.title('Airplanes Hangar Database Management System')

# # Create a select box for the tables
# table = st.selectbox('Choose a table', ['airplane', 'hanger', 'maintainance_record', 'personnel', 'hanger_location', 'personnel_contact', 'works'])

# # When a table is selected, display the contents
# if table:
#     query = f'SELECT * FROM {table}'
#     df = pd.read_sql_query(query, conn)
#     st.dataframe(df)

# # Create a text input box for SQL queries
# query = st.text_input("Enter your SQL query")

# # Execute the query and display the result
# if query:
#     try:
#         result = pd.read_sql_query(query, conn)
#         st.dataframe(result)
#     except Exception as e:
#         st.write(f'Error: {e}')

import streamlit as st
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('hangar.db')

# Title of the app
st.title('Airplanes Hangar Database Management System')

# Create a form for the airplane table
with st.form(key='airplane_form'):
    st.subheader('Add a new airplane')
    reg_no = st.number_input('Registration Number', min_value=1)
    model = st.text_input('Model')
    manufacturer = st.text_input('Manufacturer')
    status = st.text_input('Status')
    submit_button = st.form_submit_button(label='Insert')

# Insert the input data into the airplane table
# if submit_button:
#     conn.execute(f"""
#     INSERT INTO airplane (reg_no, model, manufacturer, status) 
#     VALUES ({reg_no}, '{model}', '{manufacturer}', '{status}')
#     """)
#     conn.commit()
if submit_button:
    try:
        conn.execute(f"""
        INSERT INTO airplane (reg_no, model, manufacturer, status) 
        VALUES ({reg_no}, '{model}', '{manufacturer}', '{status}')
        """)
        conn.commit()
    except sqlite3.IntegrityError:
        st.write("Error: Registration number already exists.")