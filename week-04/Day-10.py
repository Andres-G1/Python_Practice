#Day-10 on python
''' Hi :), this is Day-10 in Python.
Congratulations for reaching Day-10.
In this day you are learning classes and inheritance.
'''

# Classes
# What is a class?
''' A class is a template for creating objects.
An object is an instance with data (attributes) and behavior (methods).
'''

#a. class
#b. __init__ constructor
#c. attributes and methods
#d. inheritance and super()

# ---- BASIC CLASS ----
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} is a {self.species}.")

    def describe(self):
        print(f"Name: {self.name}, Species: {self.species}")


# ---- SUBCLASS AND INHERITANCE ----
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "dog")
        self.breed = breed

    def speak(self):
        print(f"{self.name} says: Woof!")

    def show_breed(self):
        print(f"{self.name} is a {self.breed}.")


# ---- USING THE CLASSES ----
pet = Dog("Luna", "Labrador")
pet.describe()
pet.speak()
pet.show_breed()

print("Is it an instance of Dog?", isinstance(pet, Dog))
print("Is it an instance of Animal?", isinstance(pet, Animal))
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))


# ---- ADDITIONAL EXPLANATION ----
'''
- __init__ is the constructor that receives attributes.
- self is the reference to the current object.
- super() calls the parent class constructor.
- Subclasses can override inherited methods.
'''


# ---- EXERCISES ----
# (1) Create a class called Vehicle with attributes brand, model, and year.
# (2) Create a subclass Car that inherits from Vehicle and adds a show_info() method.
# (3) Create a Car object and print its data.
# (4) Explain the behavior using comments (# or ''').

# if you complete the exercise upload the exercise to GitHub using git as intermediary,
# and share the link to the teacher.

# Congratulations you completed Day-10.
