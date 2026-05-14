 Clinic Management System Database

This project is a database system designed to manage clinic operations.

The database stores information about:
- Departments
- Clinics
- Doctors
- Patients
- Appointments

The system allows scheduling appointments and managing patient records using SQL queries.

## Features
- Manage doctors and patients
- Schedule appointments
- Prevent double booking using SQL triggers
- Validate appointment times
- Prevent scheduling appointments in the past
- Require diagnosis before completing appointments

## Technologies Used
- MySQL
- MySQL Workbench
- Python

## Triggers Implemented
1. prevent_double_booking
2. prevent_past_appointments
3. check_appointment_times
4. require_diagnosis_on_completion

## How to Run
1. Open MySQL Workbench
2. Run the SQL files inside the `sql` folder
3. Run the Python application from the `src` folder

## Author
Fatma El Warraky
