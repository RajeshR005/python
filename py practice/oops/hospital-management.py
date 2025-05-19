# Task: Create a Hospital Management System
# Create a Person class:

# Attributes: name, age, gender, address

# Methods:

# __str__() method to return a string representation of the person (name, age, gender, address)

# Create a Patient class (inherits from Person):

# Additional Attributes: patient_id, medical_history

# Methods:

# add_medical_history() method to add medical history.

# get_medical_history() method to retrieve medical history.

# __str__() method should override the one from the Person class to display patient-specific info.

# Create a Doctor class (inherits from Person):

# Additional Attributes: doctor_id, specialization

# Methods:

# diagnose() method that returns a diagnosis based on a condition.

# __str__() method should override the one from the Person class to display doctor-specific info.

# Create a Hospital class:

# Attributes: hospital_name, patients (list of patient objects), doctors (list of doctor objects)

# Methods:

# add_patient() method to add a patient to the list.

# assign_doctor() method to assign a doctor to a patient.

# get_all_patients() method to list all patients.

# __str__() method to return the hospital name and list of patients.

# Create an Appointment class (Demonstrating abstraction):

# Attributes: appointment_id, doctor, patient, date_time

# Methods:

# schedule_appointment() method to assign an appointment.

# __str__() method to display appointment details.

# Test your classes by:

# Creating instances of Patient, Doctor, Hospital, and Appointment.

# Adding patients to the hospital.

# Assigning doctors to patients.

# Scheduling appointments for patients with doctors.

# Additional Points:
# Use encapsulation to make some attributes private (e.g., medical history should not be directly accessed).

# Use polymorphism by overriding the __str__() method in Patient and Doctor to display different information.
import json

class person:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
        self.patient_data={}
    def __str__(self):
        return f"The name of the patinet is:{self.name}\nThe age of the patient is:{self.age}\nThe address of the patient is:{self.address}"
class patients(person):
    def __init__(self,age,name,gender,address,patient_id,medical_history,patient_data):
        super().__init__(name,age,gender,address,patient_data)
        self.patient_id=patient_id
        with open("\py practice\oops\hospital-management.json",'r') as f:
            self.data1=json.load(f)
        self.medical_history=medical_history
        self.patient_data.extend
        
    
p1=person("Ram",22,"M","CBE")
print(p1)
