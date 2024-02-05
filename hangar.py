import streamlit as st
import sqlite3

conn = sqlite3.connect("hangar.db")

st.title("Airplanes Hangar Database Management System")

# Creating a form for the airplane table
with st.form(key="airplane_form", clear_on_submit=False):
    st.subheader("Add a new airplane")
    reg_no = st.number_input("Registration Number *", min_value=1)
    model = st.text_input("Model *")
    manufacturer = st.text_input("Manufacturer *")
    status = st.selectbox("Status *", ("Functional", "Non-Functional"), index=None,
                          placeholder="---SELECT ANY OF THE CHOICES---")

    airplane_submit_button = st.form_submit_button(label="Insert")

if airplane_submit_button:
    try:
        if not (reg_no and model and manufacturer and status):
            st.warning("Please fill all the required fields")
        else:
            conn.execute(f"""
            INSERT INTO airplane (reg_no, model, manufacturer, status) 
            VALUES ({reg_no}, '{model}', '{manufacturer}', '{status}')
            """)
            conn.commit()
            st.success("Data has been successfully inserted!", icon='✅')
    except sqlite3.IntegrityError:
        st.warning("Error: Registration number already exists.")

# Creating a form for the Hangar
with st.form(key='hangar_form', clear_on_submit=False):
    st.subheader("Add a new Hangar")
    hangar_id = st.text_input("Hangar ID *")
    status = st.selectbox('Status *', ("Active", "Inactive"), index=None, placeholder="---SELECT ANY OF THE CHOICES---")
    capacity = st.text_input("Capacity *")

    # Query the database for existing airplane registration numbers
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT reg_no FROM airplane")
    rows = cursor.fetchall()
    reg_nos = [row['reg_no'] for row in rows]
    reg_no = st.selectbox('Airplane Registration Number *', reg_nos)

    # If the reg_no is already present in the hangar, I should prevent it from further using since its already in use
    # cursor.execute("SELECT reg_no FROM hanger")
    # column = cursor.fetchall()
    # column_nos = [column['reg_no'] for columns in column]

    hangar_submit_button = st.form_submit_button(label="Insert")

if hangar_submit_button:
    try:
        if not (hangar_id and status and capacity and reg_no):
            st.warning("Please fill all the fields before Submitting")
        else:
            conn.execute(f"""
            INSERT INTO hanger (hanger_id, status, capacity, reg_no) 
            VALUES ('{hangar_id}', '{status}', '{capacity}', {reg_no})
            """)
            conn.commit()
            st.success("Data has been successfully inserted!", icon='✅')
    except sqlite3.IntegrityError:
        st.warning("Error: Hangar ID already exists.")

with st.form(key='location_form', clear_on_submit=False):
    st.subheader("Add the location Sector and direction")
    sector = st.selectbox("Sector *", ("A", "B", "C", "D"), index=None, placeholder="---SELECT THE SECTOR---")
    direction = st.selectbox("Directions *", ("North", "South", "East", "West",
                                              "North-East (NE)", "South-East (SE)", "South-West (SW)",
                                              "North-West(NW)"), index=None,
                             placeholder="---SELECT THE DIRECTION TO THE SECTOR---")

    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT hanger_id FROM hanger")
    hanger_row = cursor.fetchall()
    hangar_nos = [row['hanger_id'] for row in hanger_row]
    hangar_no = st.selectbox("Airplane Hangar ID *", hangar_nos)

    location_submit_button = st.form_submit_button(label='Insert')

if location_submit_button:
    try:
        if not (sector and direction and hangar_no):
            st.warning("Please fill all the fields")
        else:
            conn.execute(f"""
            INSERT INTO hanger_location (sector, direction, hanger_id)
            VALUES ('{sector}', '{direction}', '{hangar_no}')
            """)
            conn.commit()
            st.success("Data has been successfully inserted!", icon='✅')
    except sqlite3.IntegrityError:
        st.warning("Error: Hangar_ID, Sector and Direction already exists")

# Creating a form for personal information
with st.form(key='personal_form', clear_on_submit=False):
    st.subheader("Add a personal information")
    emp_id = st.number_input("Employee ID *", min_value=1000)
    name = st.text_input("Name *")
    position = st.selectbox("Employee Position *", ("Worker", 'Hangar Manager', 'Quality Control Manager',
                                                    'Operations Manager', 'Associate Manager', 'Director',
                                                    'Inventory Manager', 'Director of Product Management'),
                            index=None,
                            placeholder="---SELECT YOUR POSITION---")

    personal_submit_button = st.form_submit_button(label="Insert")

if personal_submit_button:
    try:
        if not (emp_id and name and position):
            st.warning("Please fill the fields")
        else:
            conn.execute(f"""
            INSERT INTO personnel (emp_id, name, position)
            VALUES ('{emp_id}', '{name}', '{position}')
            """)
            conn.commit()
            st.success("Data has been successfully inserted!", icon='✅')
    except sqlite3.IntegrityError:
        st.warning("Employee ID already exists")
