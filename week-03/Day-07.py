#Day-07 on python
''' Hi :), this is the Day-07 on python
congratulations bypass the Day-06,
in this Day you learning loops/bucles/ciclos
'''

#Loops
#¿What is a loop?
''' A loop is a structure that repeats a block of code
while a condition is True, or for each item in a sequence.
'''

#a. while
#b. for
#c. break and continue
#d. range()

# ---- WHILE LOOP ----
'''
while condition:
    print    (This is the structure of while loop.)
'''

# Basic while: counts from 1 to 5
counter = 1
while counter <= 5:
    print("Count:", counter)
    counter += 1  # IMPORTANT: always update the variable, or it loops forever!

# While with break: stops when it finds number 3
number = 0
while True:
    number += 1
    if number == 3:
        print("Found the number 3, stopping!")
        break

# While with continue: skips number 4
num = 0
while num < 6:
    num += 1
    if num == 4:
        continue  # skip printing 4
    print("Number:", num)


# ---- FOR LOOP ----
'''
for variable in sequence:
    print    (This is the structure of for loop.)
'''

# For with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# For with range()
# range(start, stop, step)
for i in range(1, 6):      # 1 to 5
    print("i =", i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step of 2)
    print("Even:", i)

# For with break
for i in range(10):
    if i == 5:
        print("Reached 5, breaking!")
        break
    print(i)

# For with continue
for i in range(6):
    if i == 3:
        continue  # skip 3
    print("Value:", i)


# ---- EXERCISES ----

#(1) Create two exercises with while.
#(2) Create two exercises with for.
#(3) Use at least one break or continue in your exercises.
#(4) Explain the code using (# or ''')

# if you complete the exercise up the exercise to github using git as intermediary,
# and share the link to the teacher.

#Congratulations you complete the Day-07.