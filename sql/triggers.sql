USE clinc2;

DROP TRIGGER IF EXISTS prevent_double_booking;
DROP TRIGGER IF EXISTS require_diagnosis_on_completion;
DROP TRIGGER IF EXISTS prevent_past_appointments;
DROP TRIGGER IF EXISTS check_appointment_times;

DELIMITER //

CREATE TRIGGER prevent_double_booking
BEFORE INSERT ON Appointment
FOR EACH ROW
BEGIN
    DECLARE conflict_count INT;
    
    SELECT COUNT(*) INTO conflict_count
    FROM Appointment
    WHERE doctor_id = NEW.doctor_id
      AND appt_date = NEW.appt_date
      AND (
          (NEW.start_time BETWEEN start_time AND end_time) OR
          (NEW.end_time BETWEEN start_time AND end_time) OR
          (start_time BETWEEN NEW.start_time AND NEW.end_time)
      );
    
    IF conflict_count > 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Doctor already has an appointment at this time';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER require_diagnosis_on_completion
BEFORE UPDATE ON Appointment
FOR EACH ROW
BEGIN
    IF NEW.status = 'completed' AND (NEW.diagnosis IS NULL OR NEW.diagnosis = '') THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Please enter a diagnosis before completing';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER prevent_past_appointments
BEFORE INSERT ON Appointment
FOR EACH ROW
BEGIN
    IF NEW.appt_date < CURDATE() THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Cannot schedule appointments in the past';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER check_appointment_times
BEFORE INSERT ON Appointment
FOR EACH ROW
BEGIN
    IF NEW.start_time >= NEW.end_time THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Start time must be before end time';
    END IF;
END //

DELIMITER ;

SHOW TRIGGERS;
