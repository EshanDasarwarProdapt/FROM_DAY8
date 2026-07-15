# models/appointment.py

class Appointment:
    def __init__(self, id, patient_id, doctor_id, date):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date

    def display_info(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date": self.date
        }