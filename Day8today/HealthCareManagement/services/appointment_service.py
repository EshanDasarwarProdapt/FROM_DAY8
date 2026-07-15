# services/appointment_service.py

class AppointmentService:
    def __init__(self, datastore):
        self.datastore = datastore

    def add_appointment(self, appointment):
        # Check whether patient exists
        if appointment.patient_id not in self.datastore["patients"]:
            return False

        # Check whether doctor exists
        if appointment.doctor_id not in self.datastore["doctors"]:
            return False

        self.datastore["appointments"][appointment.id] = appointment
        return True

    def get_appointment(self, appointment_id):
        appointment = self.datastore["appointments"].get(appointment_id)
        if appointment:
            return appointment.display_info()
        return None

    def update_appointment(self, appointment_id, date):
        if appointment_id in self.datastore["appointments"]:
            self.datastore["appointments"][appointment_id].date = date
            return True
        return False

    def delete_appointment(self, appointment_id):
        if appointment_id in self.datastore["appointments"]:
            del self.datastore["appointments"][appointment_id]
            return True
        return False

    def get_all_appointments(self):
        return [
            appointment.display_info()
            for appointment in self.datastore["appointments"].values()
        ]