#Day-05 on python 
''' Hi :), this is the Day-05 on python
congratulations bypass the Day-04
'''
#Dicctionaries, tuple, sets and list

#¿What is the Dicctionari?
#a. info = {"name":"Andres"}
#b. info = {"Andres"}
#c. info = ("Andres")

info = {"name":"Andres"} #use this to Dicctionari
print(type(info))

#¿What is the List?
#a. info = {"Andres"}
#b. info = ("Andres")
#c. info = ["Andres"]

info = ["Andres"]
print(type(info))

#¿What is the tuple?
#a. info = {"name":"Andres"}
#b. info = {"Andres"}
#c. info = ("Andres")

info = ("Andres",17)
print(type(info))

#¿What is the sets?
#a. info = {"Andres"}
#b. info = ("Andres")
#c. info = ["Andres"]

info = {"Andres","anothers"}
print(type(info))

#Use of Dicctionari:

info_user = {
    "name" : "Andres",
    "password" : 123, 
    "ID" : "1141716845",
    "Phonenumber" : "3242709797", 
}

print(info_user["name"])
print(info_user["password"])

#create the function

Name_u = (input("Write your Username: "))
Password_u = int(input("Write your Password: "))

if Name_u in info_user["name"] and Password_u == info_user["password"]:
    print(f"Welcome {Name_u}")
else: 
    print("incorrect Password or Username")