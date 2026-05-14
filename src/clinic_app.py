import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'clinc2',
    'autocommit': True
}

COLORS = {
    'primary': '#2C3E50',
    'secondary': '#3498DB',
    'success': '#27AE60',
    'danger': '#E74C3C',
    'warning': '#F39C12',
    'light': '#ECF0F1',
    'white': '#FFFFFF'
}

class ClinicManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Clinic Management System')
        self.root.geometry('1400x800')
        self.root.configure(bg=COLORS['light'])

        self.connect_db()
        self.create_tables()
        self.create_gui()
        self.load_patients()

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def connect_db(self):
        try:
            self.conn = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
            print("Database connected successfully!")  # Debug message
        except Error as e:
            messagebox.showerror('Database Error', f"Connection failed: {str(e)}")
            print(f"Database connection error: {e}")

    def ensure_connection(self):
        try:
            if not self.conn.is_connected():
                self.conn.reconnect(attempts=3, delay=2)
                self.cursor = self.conn.cursor()
        except:
            self.connect_db()

    def create_tables(self):
        queries = [
            '''CREATE TABLE IF NOT EXISTS clinic (
                clinic_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                address VARCHAR(200)
            )''',

            '''CREATE TABLE IF NOT EXISTS department (
                dept_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                clinic_id INT,
                FOREIGN KEY (clinic_id) REFERENCES clinic(clinic_id)
            )''',

            '''CREATE TABLE IF NOT EXISTS doctor (
                doctor_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(20),
                address VARCHAR(200),
                dept_id INT,
                FOREIGN KEY (dept_id) REFERENCES department(dept_id)
            )''',

            '''CREATE TABLE IF NOT EXISTS patient (
                patient_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                birth_date DATE,
                phone VARCHAR(20),
                address VARCHAR(200),
                job VARCHAR(100)
            )''',

            '''CREATE TABLE IF NOT EXISTS appointment (
                appt_id INT PRIMARY KEY AUTO_INCREMENT,
                patient_id INT,
                doctor_id INT,
                appt_date DATE,
                start_time TIME,
                end_time TIME,
                diagnosis TEXT,
                status VARCHAR(50),
                cost DECIMAL(10,2),
                FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
                FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
            )'''
        ]

        for query in queries:
            try:
                self.cursor.execute(query)
            except Error as e:
                print(f"Error creating table: {e}")

    def create_gui(self):
        title = tk.Label(
            self.root,
            text='Clinic Management System',
            font=('Arial', 24, 'bold'),
            bg=COLORS['primary'],
            fg='white',
            pady=15
        )
        title.pack(fill='x')

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.patient_tab = tk.Frame(notebook, bg='white')
        self.appointment_tab = tk.Frame(notebook, bg='white')

        notebook.add(self.patient_tab, text='Patients')
        notebook.add(self.appointment_tab, text='Appointments')

        self.create_patient_tab()
        self.create_appointment_tab()

    def create_patient_tab(self):
        form = tk.LabelFrame(self.patient_tab, text='Patient Information', font=('Arial', 12, 'bold'))
        form.pack(fill='x', padx=10, pady=10)

        labels = ['Name', 'Birth Date (YYYY-MM-DD)', 'Phone', 'Address', 'Job']
        self.patient_entries = {}

        for i, label in enumerate(labels):
            tk.Label(form, text=label, font=('Arial', 11)).grid(row=i, column=0, padx=10, pady=8, sticky='w')
            entry = tk.Entry(form, width=40, font=('Arial', 11))
            entry.grid(row=i, column=1, padx=10, pady=8)
            self.patient_entries[label] = entry

        btn_frame = tk.Frame(form)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=15)

        tk.Button(btn_frame, text='Add Patient', command=self.add_patient,
                  bg=COLORS['success'], fg='white', width=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text='Refresh', command=self.load_patients,
                  bg=COLORS['secondary'], fg='white', width=15).pack(side='left', padx=5)

        columns = ('ID', 'Name', 'phone ', 'Adress', 'Birth Date', 'Job')
        self.patient_tree = ttk.Treeview(self.patient_tab, columns=columns, show='headings', height=15)

        for col in columns:
            self.patient_tree.heading(col, text=col)
            self.patient_tree.column(col, width=180)

        self.patient_tree.pack(fill='both', expand=True, padx=10, pady=10)

    def create_appointment_tab(self):
        frame = tk.LabelFrame(self.appointment_tab, text='Appointment Information', font=('Arial', 12, 'bold'))
        frame.pack(fill='x', padx=10, pady=10)

        # Fixed field names - added Appointment Date field
        fields = ['Patient ID', 'Doctor ID', 'Appointment Date (YYYY-MM-DD)', 
                  'Start Time (HH:MM:SS)', 'End Time (HH:MM:SS)', 
                  'Diagnosis', 'Status', 'Cost']
        self.appt_entries = {}

        for i, field in enumerate(fields):
            tk.Label(frame, text=field, font=('Arial', 11)).grid(row=i, column=0, padx=10, pady=5, sticky='w')
            entry = tk.Entry(frame, width=40, font=('Arial', 11))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.appt_entries[field] = entry

        # Add some example status options
        status_options = ['Scheduled', 'Completed']
        status_combo = ttk.Combobox(frame, values=status_options, width=37)
        status_combo.grid(row=fields.index('Status'), column=1, padx=10, pady=5)
        self.appt_entries['Status'] = status_combo

        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=len(fields), column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text='Add Appointment', command=self.add_appointment,
                  bg=COLORS['warning'], fg='white', width=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text='Clear', command=self.clear_appointment_fields,
                  bg=COLORS['secondary'], fg='white', width=15).pack(side='left', padx=5)

        # Add treeview for appointments
        appt_columns = ('ID', 'Date ', 'Patient ID', 'Doctor ID', 'Start', 'End', 'cost', 'Status')
        self.appointment_tree = ttk.Treeview(self.appointment_tab, columns=appt_columns, show='headings', height=10)
        
        for col in appt_columns:
            self.appointment_tree.heading(col, text=col)
            self.appointment_tree.column(col, width=120)
        
        self.appointment_tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Button(self.appointment_tab, text='Load Appointments', command=self.load_appointments,
                  bg=COLORS['primary'], fg='white', width=20).pack(pady=5)

    def add_patient(self):
        try:
            self.ensure_connection()
            
            # Get values with the correct key name
            birth_date = self.patient_entries['Birth Date (YYYY-MM-DD)'].get()
            
            # Validate date format
            if birth_date:
                try:
                    datetime.strptime(birth_date, '%Y-%m-%d')
                except ValueError:
                    messagebox.showerror('Error', 'Birth date must be in YYYY-MM-DD format')
                    return
            
            values = (
                self.patient_entries['Name'].get(),
                birth_date if birth_date else None,
                self.patient_entries['Phone'].get(),
                self.patient_entries['Address'].get(),
                self.patient_entries['Job'].get()
            )

            query = '''INSERT INTO patient (name, birth_date, phone, address, job)
                       VALUES (%s, %s, %s, %s, %s)'''
            self.cursor.execute(query, values)
            self.conn.commit()

            messagebox.showinfo('Success', 'Patient added successfully!')
            self.clear_patient_fields()
            self.load_patients()

        except Error as e:
            messagebox.showerror('Database Error', f"Error adding patient: {str(e)}")
            print(f"SQL Error: {e}")

    def add_appointment(self):
        try:
            self.ensure_connection()
            
            # Get values with correct field names
            appt_date = self.appt_entries['Appointment Date (YYYY-MM-DD)'].get()
            start_time = self.appt_entries['Start Time (HH:MM:SS)'].get()
            end_time = self.appt_entries['End Time (HH:MM:SS)'].get()
            
            # Validate date format
            try:
                if appt_date:
                    datetime.strptime(appt_date, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror('Error', 'Appointment date must be in YYYY-MM-DD format')
                return
            
            # Get status from combobox
            status = self.appt_entries['Status'].get() if hasattr(self.appt_entries['Status'], 'get') else self.appt_entries['Status']
            
            values = (
                int(self.appt_entries['Patient ID'].get()),
                int(self.appt_entries['Doctor ID'].get()),
                appt_date,
                start_time,
                end_time,
                self.appt_entries['Diagnosis'].get(),
                status,
                float(self.appt_entries['Cost'].get()) if self.appt_entries['Cost'].get() else 0
            )

            query = '''INSERT INTO appointment
                       (patient_id, doctor_id, appt_date, start_time, end_time, diagnosis, status, cost)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
            self.cursor.execute(query, values)
            self.conn.commit()

            messagebox.showinfo('Success', 'Appointment added successfully!')
            self.clear_appointment_fields()
            self.load_appointments()

        except ValueError as e:
            messagebox.showerror('Error', f'Invalid input: {str(e)}')
        except Error as e:
            messagebox.showerror('Database Error', f"Error adding appointment: {str(e)}")
            print(f"SQL Error: {e}")

    def load_patients(self):
        try:
            self.ensure_connection()

            for item in self.patient_tree.get_children():
                self.patient_tree.delete(item)

            self.cursor.execute('SELECT * FROM patient')
            rows = self.cursor.fetchall()

            for row in rows:
                self.patient_tree.insert('', 'end', values=row)
            
            print(f"Loaded {len(rows)} patients")  # Debug message

        except Error as e:
            messagebox.showerror('Error', f"Error loading patients: {str(e)}")

    def load_appointments(self):
        try:
            self.ensure_connection()

            for item in self.appointment_tree.get_children():
                self.appointment_tree.delete(item)

            self.cursor.execute('SELECT * FROM appointment')
            rows = self.cursor.fetchall()

            for row in rows:
                self.appointment_tree.insert('', 'end', values=row)
            
            print(f"Loaded {len(rows)} appointments")  # Debug message

        except Error as e:
            messagebox.showerror('Error', f"Error loading appointments: {str(e)}")

    def clear_patient_fields(self):
        for entry in self.patient_entries.values():
            entry.delete(0, tk.END)

    def clear_appointment_fields(self):
        for entry in self.appt_entries.values():
            if hasattr(entry, 'delete'):
                entry.delete(0, tk.END)
            elif hasattr(entry, 'set'):
                entry.set('')

    def on_closing(self):
        if hasattr(self, 'conn') and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
        self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = ClinicManagementSystem(root)
    root.mainloop()
