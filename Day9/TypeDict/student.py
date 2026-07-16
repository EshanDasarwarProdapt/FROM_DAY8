from typing import TypedDict

class Student(TypedDict):
    id: int
    name: str
    age: int

student1 = Student(id=1, name="Alice", age=20)
student2 = Student(id=101, name="BOB", age=23)

print(student1)
print(student2)

#TypedDict will covert the result into a dictionary format.
#mypy catches the error before you run the program
