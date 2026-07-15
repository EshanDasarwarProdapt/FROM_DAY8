class PatientService:
    def __init__(self,datastore):
        self.datastore = datastore

    def add_patient(self,patient):
        # Use the public id attribute from Person/Patient.
        self.datastore["patients"][patient.id] = patient

    def get_patient(self,patient_id):
        patient = self.datastore["patients"].get(patient_id)
        if patient:
            return patient.display_info()
        return None
    
    def update_patient(self,patient_id, ailment):
        if patient_id in self.datastore["patients"]:
            self.datastore["patients"][patient_id].ailment = ailment
            return True
        return False
    
    def delete_patient(self,patient_id):
        if patient_id in self.datastore["patients"]:
            del self.datastore["patients"][patient_id]
            return True
        return False