#Day-04 on python 
''' Hi :), this is the Day-04 on python
congratulations bypass the Day-03,
in this Day you learning conditionals
'''
#Conditionals
#¿What is conditional?

#a. if else
#b. case
#c. $is else
'''
if:
    print    (This is the structure of conditional.)
else:
    print 
'''

#And use the others: variables and print whit the conditional

age = 17
if age >= 18:
    print("You are old")
else:
    print("You are not old")

#Use of elif

Age = 18
if Age >= 1 and age < 3:
    print("You are baby")
elif Age >= 3 and age < 14:
    print("You are kid")
elif Age >= 14 and age < 18:
    print("You are teenager")
elif Age > 18 and age < 30:
    print("You are adult")
else:
    print("You are old")