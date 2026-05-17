CREATE DATABASE clinc2;
USE clinc2 ;
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Clinic (
    clinic_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Doctor (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    birth_date DATE,
    job VARCHAR(100)
);

CREATE TABLE Appointment (
    appt_id INT PRIMARY KEY AUTO_INCREMENT,
    appt_date DATE NOT NULL,
    patient_id INT,
    doctor_id INT,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('scheduled', 'in progress', 'postponed')),
    diagnosis TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
);
