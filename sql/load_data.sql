USE clinc2;
INSERT INTO Department VALUES
(1, 'Cardiology'), (2, 'Neurology'), (3, 'Pediatrics'), (4, 'Orthopedics'),
(5, 'Dermatology'), (6, 'Ophthalmology'), (7, 'ENT'), (8, 'Psychiatry'),
(9, 'Urology'), (10, 'Gastroenterology');

INSERT INTO Clinic VALUES
(1, 'Heart Clinic North', '123 Main St', 1),
(2, 'Brain Center', '456 Oak Ave', 2),
(3, 'Kids Care', '789 Pine Rd', 3),
(4, 'Bone & Joint', '321 Elm Blvd', 4),
(5, 'Skin Health', '654 Maple Dr', 5),
(6, 'Vision Plus', '987 Cedar Ln', 6),
(7, 'Ear Nose Throat', '147 Birch Way', 7),
(8, 'Mind Wellness', '258 Spruce Ct', 8),
(9, 'Kidney Care', '369 Ash St', 9),
(10, 'Digestive Health', '741 Willow Ave', 10);

INSERT INTO Doctor VALUES
(101, 'Dr. Ahmed Ali', '555-0101', '123 Medical Blvd', 1),
(102, 'Dr. Sara Hassan', '555-0102', '456 Health St', 1),
(103, 'Dr. Khaled Omar', '555-0103', '789 Wellness Rd', 2),
(104, 'Dr. Lina Tamer', '555-0104', '321 Care Ave', 3),
(105, 'Dr. Mona Fouad', '555-0105', '654 Cure Ln', 4),
(106, 'Dr. Youssef Nabil', '555-0106', '987 Remedy Dr', 5),
(107, 'Dr. Nour Adel', '555-0107', '147 Therapy Ct', 6),
(108, 'Dr. Omar Sherif', '555-0108', '258 Healing Way', 7),
(109, 'Dr. Hana Magdy', '555-0109', '369 Recovery St', 8),
(110, 'Dr. Ziad Lotfy', '555-0110', '741 Hope Blvd', 9);

INSERT INTO Patient VALUES
(1001, 'Mohamed Ibrahim', '555-1001', '10 Nile St', '1980-05-15', 'Engineer'),
(1002, 'Fatima Hassan', '555-1002', '20 Pyramids Rd', '1992-08-22', 'Teacher'),
(1003, 'Omar Salah', '555-1003', '30 Tahrir Sq', '1975-11-10', 'Accountant'),
(1004, 'Laila Mahmoud', '555-1004', '40 Giza St', '1988-03-05', 'Doctor'),
(1005, 'Ahmed Samir', '555-1005', '50 Heliopolis Ave', '1995-07-30', 'Student'),
(1006, 'Nadia Hossam', '555-1006', '60 Maadi St', '1983-12-25', 'Lawyer'),
(1007, 'Khaled Youssef', '555-1007', '70 Nasr City', '1970-09-14', 'Manager'),
(1008, 'Reem Tarek', '555-1008', '80 Zamalek', '2000-01-20', 'Nurse'),
(1009, 'Hany Mostafa', '555-1009', '90 Dokki St', '1965-06-18', 'Retired'),
(1010, 'Shereen Adly', '555-1010', '100 Shubra Rd', '1998-04-12', 'Designer');

INSERT INTO Appointment (appt_id, appt_date, patient_id, doctor_id, start_time, end_time, cost, status, diagnosis) VALUES
(5011, '2024-06-15', 1001, 101, '09:00:00', '09:30:00', 250.00, 'scheduled', 'Routine checkup'),
(5012, '2024-06-16', 1002, 103, '10:00:00', '10:45:00', 300.00, 'scheduled', 'Headache'),
(5013, '2024-06-17', 1003, 104, '11:00:00', '11:30:00', 200.00, 'scheduled', 'Cough'),
(5014, '2024-06-18', 1004, 105, '13:00:00', '13:45:00', 350.00, 'scheduled', 'Back pain'),
(5015, '2024-06-19', 1005, 106, '14:00:00', '14:30:00', 180.00, 'scheduled', 'Skin rash');
