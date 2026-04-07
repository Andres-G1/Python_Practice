#Day-11 on python
''' Hi :), this is Day-11 in Python.
Congratulations for reaching Day-11.
In this day you are learning modules and packages.
'''

# Modules and packages
# What is a module?
''' A module is a Python file (.py) that contains functions, classes, and variables.
A package is a folder that groups many modules.
'''

#a. import
#b. from ... import ...
#c. standard modules
#d. packages and local files

# ---- STANDARD MODULES ----
import math
import random
from datetime import datetime

print("Square root of 16:", math.sqrt(16))
print("Random number between 1 and 10:", random.randint(1, 10))
print("Current date and time:", datetime.now())


# ---- USING MODULES ----
# We can use standard modules for many tasks.

# math: math functions
value = 25
print("The absolute value of -25 is", math.fabs(-25))

# random: random numbers and selections
colors = ["red", "green", "blue"]
print("Selected color:", random.choice(colors))

# datetime: working with dates
today = datetime.today()
print(f"Today is {today.day}/{today.month}/{today.year}")


# ---- LOCAL PACKAGES ----
'''
If you create a file called helpers.py, you can import it like this:
    from helpers import my_function

To create a package, use a folder with __init__.py.
'''


# ---- EXERCISES ----
# (1) Use the math module to calculate the area of a circle.
# (2) Use random to create an 8-character password with letters and numbers.
# (3) Create a function in a separate file and import it here.
# (4) Explain the code using comments (# or ''').

# if you complete the exercise upload the exercise to GitHub using git as intermediary,
# and share the link to the teacher.

# Congratulations you completed Day-11.
