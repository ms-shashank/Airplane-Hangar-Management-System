# ✈️ Airplane Hangar Management System

## Overview

The **Airplane Hangar Management System** is a web application built using Python, Streamlit, and SQLite to manage airplane data, hangars, employee details, and maintenance records. The system is designed to streamline the process of managing multiple entities involved in an airplane hangar, including aircraft, hangar locations, employees, and maintenance activities.

## Features

- **Airplane Management**: Add new airplanes with their registration numbers, models, manufacturers, and operational status.
- **Hangar Management**: Assign airplanes to specific hangars, track hangar status, and manage hangar capacity.
- **Location Management**: Assign hangar locations by sector and direction.
- **Personnel Management**: Add employee information, assign employees to hangars, and maintain their contact details.
- **Maintenance Records**: Keep track of airplane maintenance activities, including dates and costs.

## Technologies Used

- **Backend**: SQLite3
- **Frontend**: Streamlit (Python)
- **Language**: Python

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ms-shashank/Airplane-Hangar-Management-System.git
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

## Database Structure

- **airplane**: Stores airplane details (`reg_no`, `model`, `manufacturer`, `status`).
- **hangar**: Stores hangar information (`hanger_id`, `status`, `capacity`, `reg_no`).
- **hanger_location**: Tracks hangar locations (`sector`, `direction`, `hanger_id`).
- **personnel**: Manages employee details (`emp_id`, `name`, `position`).
- **personnel_contact**: Stores contact information for employees (`phone_no`, `mail_id`, `emp_id`).
- **maintenance_record**: Records airplane maintenance details (`main_id`, `main_date`, `cost`, `reg_no`).
- **works**: Maps employees to hangars (`emp_id`, `hanger_id`).

## Usage

1. **Add Airplane**: Input airplane details such as registration number, model, manufacturer, and status.
2. **Add Hangar**: Define hangars with their status, capacity, and airplane registration number.
3. **Add Location**: Specify the sector and direction of each hangar.
4. **Add Employee**: Input employee details and assign them to a hangar.
5. **Add Maintenance Record**: Track maintenance records for each airplane.


## Contributing

Feel free to open issues and submit pull requests if you'd like to contribute to this project.
