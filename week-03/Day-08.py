#Day-08 on python
''' Hi :), this is the Day-08 on python
congratulations bypass the Day-07,
in this Day you learning functions
'''

#Functions
#¿What is a function?
''' A function is a reusable block of code that performs a specific task.
You define it once and call it as many times as you need.
'''

#a. def (define a function)
#b. parameters and arguments
#c. return
#d. default parameters

# ---- BASIC FUNCTION ----
'''
def function_name():
    print    (This is the structure of a function.)
'''

# Simple function with no parameters
def greet():
    print("Hello! Welcome to Day-06.")

greet()  # calling the function


# ---- FUNCTION WITH PARAMETERS ----
'''
def function_name(parameter):
    print(parameter)
'''

# Function that receives a name
def greet_person(name):
    print("Hello,", name + "!")

greet_person("Carlos")
greet_person("Maria")


# ---- FUNCTION WITH RETURN ----
''' return sends a value back to whoever called the function.
Without return, the function returns None by default.
'''

# Function that adds two numbers and returns the result
def add(a, b):
    result = a + b
    return result

total = add(5, 3)
print("Total:", total)

# Function that checks if a number is even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(4))   # Even
print(even_or_odd(7))   # Odd


# ---- DEFAULT PARAMETERS ----
''' You can assign a default value to a parameter.
If the caller doesn't pass that argument, the default is used.
'''

def greet_language(name, language="English"):
    if language == "Spanish":
        print("Hola,", name + "!")
    else:
        print("Hello,", name + "!")

greet_language("Ana")              # uses default: English
greet_language("Luis", "Spanish")  # uses Spanish


# ---- FUNCTION WITH MULTIPLE RETURNS ----

# Function that returns the area and perimeter of a rectangle
def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

area, perimeter = rectangle(5, 3)
print("Area:", area)
print("Perimeter:", perimeter)


# ---- EXERCISES ----

#(1) Create a function that receives two numbers and returns the multiplication.
#(2) Create a function that receives a name and age, and prints a greeting.
#(3) Create a function that uses a loop inside to print a multiplication table.
#(4) Explain the code using (# or ''')

# if you complete the exercise up the exercise to github using git as intermediary,
# and share the link to the teacher.

#Congratulations you complete the Day-08.