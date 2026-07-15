# models/doctor.py

from models.person import Person

class Doctor(Person):
    def __init__(self, id, name, age, specialization):
        super().__init__(id, name, age)
        self.specialization = specialization

    def display_info(self):
        details = super().display_info()
        details.update({
            "specialization": self.specialization
        })
        return details