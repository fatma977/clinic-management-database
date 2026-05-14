USE clinc2;

-- Query 1
SELECT p.name, a.diagnosis
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
WHERE a.diagnosis = 'Fatty liver disease';

-- Query 2
SELECT c.clinic_id, c.name, c.address
FROM Clinic c
JOIN Department d ON c.dept_id = d.dept_id
WHERE d.name = 'Cardiology';

-- Query 3
SELECT 
    p.patient_id,
    p.name,
    COUNT(a.appt_id) AS total_visits,
    SUM(a.cost) AS total_paid
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
WHERE p.patient_id = 1002
  AND a.appt_date >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
GROUP BY p.patient_id, p.name;
