#Exercice 1:
#Print height
height = int(input("write the height: "))

#Read height
print(f"the height is {height}cm ")

#calculate in pulgates
# en pulgadas igual muchachos :)
#aca coloque lo de la variable en este caso
#en este solo colocamos la variable de altura
#y la dividimos por el valor de pulgadas
#seguido de ya tener el valor de pulgadas
#lo hacemos con el valor de pies :)
height_pulg = height / 2.54
height_feet = height_pulg / 12

#despues lo imprimimos el resultado
print (f"the height in pulgates is {height_pulg} ")
print (f"the height in feet is {height_feet} ")

#y ya estaria el primer ejercicio o bueno la primera parte

#Exercice 2:
#area of triangle
base = int(input("write the base of the triangle: "))
height_triangle = int (input("write the height of the triangle:"))

Area = (base *height_triangle) / 2
print (f"the area of the triangle is {Area}")
#Exercice 3:
#celcius to fahrenheit
celcius = int(input("write the degrees celcius: "))
farenheit = (celcius * 9/5) + 32
print (f"the degrees in farenheit is {farenheit}")

#Exercice 4:
#name and pasword
name = (input("write your name: "))
pasword = (input("write your pasword: "))
print(f"welcome your name is {name} and your pasword is {pasword}")


#my example
infous = {
    "name": "Sebastian",
    "pasword": "123",
}

names =  (input("Write your name: "))
paswords = (input("write your pasword: "))

if names == infous["name"] and paswords == infous["pasword"]:
    print(f"welcome back, {names}")
else:
    print("the name or pasword is incorrect")


