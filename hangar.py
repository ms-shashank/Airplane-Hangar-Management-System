import streamlit as st
import sqlite3

st.set_page_config(layout="wide")

conn = sqlite3.connect("hangar.db")

st.title(":blue[Airplanes] ✈️ Hangar Database Management System", anchor=False)

st.divider()
# Creating a form for the airplane table

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Add Airplanes", 
                                        "Add Hangar",
                                        "Add Personal information",
                                        "Workers in Hangar",
                                        "Peronnel info of workers",
                                        "Mainenance Record"])

st.divider()

with tab1:
    with st.form(key="airplane_form", clear_on_submit=False):
        st.header(":violet[Add a new airplane]", anchor=False, divider="rainbow")
        reg_no = st.number_input("Registration Number *", min_value=1)
        model = st.text_input("Model *")
        manufacturer = st.text_input("Manufacturer *")
        status = st.selectbox("Status *", ("Functional", "Non-Functional"), index=None,
                            placeholder="---SELECT ANY OF THE CHOICES---")

        airplane_submit_button = st.form_submit_button(label="Submit")

    if airplane_submit_button:
        try:
            if not (reg_no and model and manufacturer and status):
                st.warning("Please fill all the required fields", icon='⚠️')
            else:
                conn.execute(f"""
                INSERT INTO airplane (reg_no, model, manufacturer, status) 
                VALUES ({reg_no}, '{model}', '{manufacturer}', '{status}')
                """)
                conn.commit()
                st.success("Data has been successfully inserted!", icon='✅')
        except sqlite3.IntegrityError:
            st.error("Error: Registration number already exists.", icon='❌')

#st.divider()


with tab2:

    col1, col2, = st.columns([3, 2])

    # Creating a form for the Hangar
    with st.container():
        with col1:
            with st.form(key='hangar_form', clear_on_submit=False):
                st.header("Add a new Hangar", anchor=False, divider="rainbow")
                hangar_id = st.text_input("Hangar ID *")
                status = st.selectbox('Status *', ("Active", "Inactive"), index=None,
                                    placeholder="---SELECT ANY OF THE CHOICES---")
                capacity = st.text_input("Capacity *")

                # Query the database for existing airplane registration numbers
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT reg_no FROM airplane")
                rows = cursor.fetchall()
                reg_nos = [row['reg_no'] for row in rows]
                reg_no = st.selectbox('Airplane Registration Number *', reg_nos)

                # If the reg_no is already present in the hangar, I should prevent it from further
                # using since its already in use
                # cursor.execute("SELECT reg_no FROM hanger")
                # column = cursor.fetchall()
                # column_nos = [column['reg_no'] for columns in column]

                hangar_submit_button = st.form_submit_button(label="Submit")

            if hangar_submit_button:
                try:
                    if not (hangar_id and status and capacity and reg_no):
                        st.warning("Please fill all the fields before Submitting", icon='⚠️')
                    else:
                        conn.execute(f"""
                        INSERT INTO hanger (hanger_id, status, capacity, reg_no) 
                        VALUES ('{hangar_id}', '{status}', '{capacity}', {reg_no})
                        """)
                        conn.commit()
                        st.success("Data has been successfully inserted!", icon='✅')
                except sqlite3.IntegrityError:
                    st.error("Error: Hangar ID already exists.", icon='❌')

        with col2:
            with st.form(key='location_form', clear_on_submit=False):
                st.header("Add the location Sector and direction", anchor=False, divider="rainbow")
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

                location_submit_button = st.form_submit_button(label='Submit')

            if location_submit_button:
                try:
                    if not (sector and direction and hangar_no):
                        st.warning("Please fill all the fields", icon='⚠️')
                    else:
                        conn.execute(f"""
                        INSERT INTO hanger_location (sector, direction, hanger_id)
                        VALUES ('{sector}', '{direction}', '{hangar_no}')
                        """)
                        conn.commit()
                        st.success("Data has been successfully inserted!", icon='✅')
                except sqlite3.IntegrityError:
                    st.error("Error: Hangar_ID, Sector and Direction already exists", icon='❌')


#st.divider()

with tab3:

    # Creating a form for personal information
    with st.form(key='personal_form', clear_on_submit=False):
        st.header("Add a personal information", anchor=False, divider="rainbow")
        emp_id = st.number_input("Employee ID *", min_value=1000)
        name = st.text_input("Name *")
        position = st.selectbox("Employee Position *", ("Worker", 'Hangar Manager', 'Quality Control Manager',
                                                        'Operations Manager', 'Associate Manager', 'Director',
                                                        'Inventory Manager', 'Director of Product Management'),
                                index=None,
                                placeholder="---SELECT YOUR POSITION---")


        personal_submit_button = st.form_submit_button(label="Submit")

    if personal_submit_button:
        try:
            if not (emp_id and name and position):
                st.warning("Please fill the fields", icon='⚠️')
            else:
                conn.execute(f"""
                INSERT INTO personnel (emp_id, name, position)
                VALUES ('{emp_id}', '{name}', '{position}')
                """)
                conn.commit()
                st.success("Data has been successfully inserted!", icon='✅')
        except sqlite3.IntegrityError:
            st.error("ERROR: Employee ID already exists", icon='❌')

#st.divider()

with tab4:
    # with st.form(key='', clear_on_submit=False):
    with st.form(key='Workers_In_Hangar', clear_on_submit=False):
        st.header("Workers in Hangar", anchor=False, divider="rainbow")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT hanger_ID FROM hanger")
        hanger_row = cursor.fetchall()
        hanger_Id_Nos = [row['hanger_ID'] for row in hanger_row]

        foreign_key_hangarId = st.selectbox("Hangar's ID ", hanger_Id_Nos)

        cursor.execute("SELECT emp_id FROM personnel")
        emp_row = cursor.fetchall()
        emp_rows = [row['emp_id'] for row in emp_row]

        foreign_key_empId = st.selectbox("Employee's ID", emp_rows)

        working_submit_button = st.form_submit_button(label="Submit")

    if working_submit_button:
        try:
            if not (foreign_key_empId and foreign_key_empId):
                st.warning("Fill all the Fields.", icon='⚠️')
            else:
                conn.execute(f"""
                INSERT INTO works (emp_id, hanger_id)
                VALUES ('{foreign_key_empId}', '{foreign_key_hangarId}')
                """)
                conn.commit()
                st.success("Data has been successfully inserted!", icon='✅')
        except sqlite3.IntegrityError:
            st.error("ERROR: Employee ID or Hangar ID already exists", icon='❌')


with tab5:

    with st.form(key="Workers_personnel_information", clear_on_submit=False):
        st.header("Worker's Personnel Information", divider="rainbow")
        phone_no = st.number_input("Enter your Phone Number *", min_value=1000000000)
        mail_id = st.text_input("Enter your Mail ID *")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id FROM personnel")
        emp_row = cursor.fetchall()
        emp_rows = [row['emp_id'] for row in emp_row]

        employee_id = st.selectbox("Employee's ID *", emp_rows)

        personnel_information = st.form_submit_button(label="Submit")

    if personnel_information:
        try:
            if not (phone_no and mail_id and employee_id):
                st.warning("Fill all the Fields", icon='⚠️')
            else:
                conn.execute(f"""
                INSERT INTO personnel_contact (phono_no, mail_id, emp_id)
                VALUES ({phone_no}, '{mail_id}',{emp_id})
                """)
                conn.commit()
                st.success("Data has been successfully inserted!", icon='✅')
        except sqlite3.IntegrityError:
            st.warning("ERROR: The Employee ID already exists", icon='⚠️')
            st.error("The Employee ID already exists", icon='❌')

with tab6:
    with st.form(key='maintenance_record', clear_on_submit=False):
        st.header("Maintenance Record of a Plane", divider='rainbow')
        main_id = st.text_input("Enter the Maintenance-ID *")
        main_date = st.date_input("Enter the date of maintenance *")
        cost = st.number_input("Enter the total maintenance cost of the airplane *", min_value=20000)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT reg_no FROM airplane")
        plane_reg_no = cursor.fetchall()
        plane_reg_nos = [row['reg_no'] for row in plane_reg_no]

        st.selectbox("Select the appropriate Airplane register number ", plane_reg_nos)

        maintenance_submit_button = st.form_submit_button(label="Submit")

    if maintenance_submit_button:
        try:
            if not (main_id and main_date and cost and reg_no):
                st.warning("Please fill all the fields", icon='⚠️')
            else:
                conn.execute(f"""
                INSERT INTO maintainance_record (main_id, main_date, cost, reg_no)
                VALUES ('{main_id}', '{main_date}', {cost} ,{reg_no})
                """)
                conn.commit()
                st.success("Data has been successfully inserted!", icon='✅')
        except sqlite3.IntegrityError:
            st.error("ERROR: Maintenance Record already exists", icon='❌')
