import streamlit as st
import sqlite3

conn = sqlite3.connect('hangar.db')

st.title('Airplanes Hangar Database Management System')

# Create a form for the airplane table
with st.form(key='airplane_form', clear_on_submit=False):
    st.subheader('Add a new airplane')
    reg_no = st.number_input('Registration Number *', min_value=1)
    model = st.text_input('Model *')
    manufacturer = st.text_input('Manufacturer *')
    status = st.selectbox('Status *', ("Functional","Non-Functional"),  index=None, placeholder="---SELECT ANY OF THE CHOICES---")

    submit_button = st.form_submit_button(label="Insert")

if submit_button:
    try:
        if not (reg_no and model and manufacturer and status):
            st.write("Please fill all the required fields")
        else:
            conn.execute(f"""
            INSERT INTO airplane (reg_no, model, manufacturer, status) 
            VALUES ({reg_no}, '{model}', '{manufacturer}', '{status}')
            """)
            conn.commit()
    except sqlite3.IntegrityError:
        st.write("Error: Registration number already exists.")

#Create a form for the Hangar
with st.form(key='hangar_form'):
    st.subheader('Add a new Hangar')
    hangar_id = st.text_input('Hangar ID *')
    status = st.selectbox('Status *', ("Active", "Inactive"), index=None, placeholder="---SELECT ANY OF THE CHOICES---")
    capacity = st.text_input('Capacity *')

    # Query the database for existing airplane registration numbers
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT reg_no FROM airplane")
    rows = cursor.fetchall()
    reg_nos = [row['reg_no'] for row in rows]
    reg_no = st.selectbox('Airplane Registration Number *', reg_nos)

    submit_button = st.form_submit_button(label='Insert')

if submit_button:
    try:
        if not (hangar_id and status and capacity and reg_no):
            st.write("Please fill all the fields before Submitting")
        else:    
            conn.execute(f"""
            INSERT INTO hanger (hanger_id, status, capacity, reg_no) 
            VALUES ('{hangar_id}', '{status}', '{capacity}', {reg_no})
            """)
            conn.commit()
    except sqlite3.IntegrityError:
        st.write("Error: Hangar ID already exists.")
