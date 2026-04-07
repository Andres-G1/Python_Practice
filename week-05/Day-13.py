#Day-13 on python
''' Hi :), this is Day-13 in Python.
Congratulations for reaching Day-13.
In this day you are learning advanced classes in Python.
'''

# Advanced classes
# What is a classmethod, staticmethod, and property?
'''
In Python classes can have:
- @classmethod: a method that receives the class as the first argument.
- @staticmethod: a function inside the class that does not receive self or cls.
- @property: converts a method into a computed attribute.
'''

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grade: int

    @property
    def approved(self):
        return self.grade >= 70

    @classmethod
    def from_string(cls, data):
        name, grade = data.split(",")
        return cls(name.strip(), int(grade.strip()))

    @staticmethod
    def welcome_message():
        return "Welcome to the student system"


# ---- USING STUDENT ----
student_1 = Student("Ana", 85)
print(student_1)
print("Approved?", student_1.approved)
print(Student.welcome_message())

student_2 = Student.from_string("Luis, 65")
print(student_2)
print("Approved?", student_2.approved)


# ---- PROPERTY ----
'''
@property allows using a method like an attribute.
This makes the code cleaner and easier to read.
'''


# ---- EXERCISES ----
# (1) Create an Employee class with name and salary attributes.
# (2) Add a @property method named annual_salary.
# (3) Create a @classmethod that builds an employee from a string.
# (4) Explain the code using comments (# or ''').

# if you complete the exercise upload the exercise to GitHub using git as intermediary,
# and share the link to the teacher.

# Congratulations you completed Day-13.
