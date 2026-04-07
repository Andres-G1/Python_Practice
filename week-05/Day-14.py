#Day-14 on python
''' Hi :), this is Day-14 in Python.
Congratulations for reaching Day-14.
In this day you are learning file handling and exceptions.
'''

# Files and exceptions
# What is file handling?
''' Reading and writing files allows you to save data between runs.
Exception handling prevents the program from stopping with unexpected errors.
'''

# ---- WRITE TO A FILE ----
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello, this is an example file.\n")
    file.write("Second line of text.\n")

print("File data.txt created successfully.")

# ---- READ FROM A FILE ----
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("The file does not exist. Make sure you run this code in the correct folder.")

# ---- EXCEPTION HANDLING ----
try:
    number = int(input("Enter a number: "))
    print("The number is", number)
except ValueError:
    print("You must enter a valid number.")
finally:
    print("End of number reading.")


# ---- EXERCISES ----
# (1) Read and display a file using with.
# (2) Add a line to the file using mode "a".
# (3) Handle ValueError when the user does not enter a number.
# (4) Explain the code using comments (# or ''').

# if you complete the exercise upload the exercise to GitHub using git as intermediary,
# and share the link to the teacher.

# Congratulations you completed Day-14.
