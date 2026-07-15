from data.datastore import datastore
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment

from services.healthcare_system import HealthcareSystem

# Create Healthcare System
system = HealthcareSystem(datastore)

# ----------------------------
# Add Patients
# ----------------------------
p1 = Patient(1, "John Doe", 30, "Flu")
p2 = Patient(2, "Jane Smith", 25, "Cold")

system.patient_service.add_patient(p1)
system.patient_service.add_patient(p2)

# ----------------------------
# Add Doctors
# ----------------------------
d1 = Doctor(101, "Dr. Alice", 45, "Cardiologist")
d2 = Doctor(102, "Dr. Bob", 50, "Dermatologist")

system.doctor_service.add_doctor(d1)
system.doctor_service.add_doctor(d2)

# ----------------------------
# Add Appointments
# ----------------------------
a1 = Appointment(1001, 1, 101, "2026-07-20")
a2 = Appointment(1002, 2, 102, "2026-07-21")

system.appointment_service.add_appointment(a1)
system.appointment_service.add_appointment(a2)

# ----------------------------
# Display Data
# ----------------------------
print("Patient:")
print(system.patient_service.get_patient(2))

print("\nDoctor:")
print(system.doctor_service.get_doctor(101))

print("\nAppointment:")
print(system.appointment_service.get_appointment(1001))

# ----------------------------
# Update Data
# ----------------------------
system.patient_service.update_patient(2, "Fever")
system.doctor_service.update_doctor(102, "Neurologist")
system.appointment_service.update_appointment(1002, "2026-07-25")

print("\nUpdated Patient:")
print(system.patient_service.get_patient(2))

print("\nUpdated Doctor:")
print(system.doctor_service.get_doctor(102))

print("\nUpdated Appointment:")
print(system.appointment_service.get_appointment(1002))

# ----------------------------
# Delete Data
# ----------------------------
system.patient_service.delete_patient(1)
system.doctor_service.delete_doctor(101)
system.appointment_service.delete_appointment(1001)

print("\nAfter Deletion:")
print(system.patient_service.get_patient(1))       # None
print(system.doctor_service.get_doctor(101))       # None
print(system.appointment_service.get_appointment(1001))  # None