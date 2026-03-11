print("Hello word")
print(type("n"))
print(type(1))
print(type(1.2))
print(type(1j))
print(type(True))
lista = []
dic = {}
tuplas = ()
sets = {()}
print(type(lista))
print(type(dic))
print(type(tuplas))
print(type(sets))

name = ("Daniel")
fullname=(input("write your name"))
print(name)
print(fullname)
print(type(fullname))

Dicc = {
"nombre" : "Sebastian",
"years" : 17
}

print(Dicc["nombre"])

x , y = 1, 2

print(x**y)
print(x%y)
print(x//y)
print(x/y)
print(x+y)

x = 5
x = x + 3
x -= 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= 3
x = 5
x &= 20
print (x)
print(x := 20)
#1
a = 15
b = 4
print(a%b)
print(a//b)
print(a**b)
a +=10
print(a)
a = 15
a += 10
print(a)

#2
num1 = int(input("write the firts number"))
num2 = int(input("write the second number"))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

nu1 = int(input("write the firts number"))
nu2 = int(input("write the second number"))
nu3 = int(input("write the thret number"))
resul= nu1+nu2+nu3 / 3
print(resul)

pre = int(input("write the price of the product"))
res = pre * 0.15
fin = pre - res
print(pre)
print(fin)

log = input("Escribe la opción: m: 1 cm: 2: ")

match log:
    case "1":
        num = float(input("Escribe el número en m: "))
        print(num * 100, "cm")
    case "2":
        num = float(input("Escribe el número en cm: "))
        print(num / 100, "m")
    case _:
        print("Opción no válida")



#example

print(1<2)
print(2>10)
print(1 != 10)
print(1==1)
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print(True or True)
print(True or False)
print(False or False)
print(False or True)

#Realizar un programa inicuo se sesion
x = 5
y = 3
if x > y:
    print("hi :D, im developer in python")
else:
    print("im bad in python :<")
    
user = (input("write the username"))
pasword = int(input("write the pasword"))
age = int(input("writhe the age"))

if age >17:
    print(f"welcome {user}  you are old ")
else:
    print("you are not old")
    
# forms to print
ficha = 3407184
curso = "ADSO"
print("Hi", ficha, "del curso", curso)
print("Hi "+ str(ficha)+ "del curso ",+curso)
print(f"Hi {ficha} del curso {curso}")
#{version:.2f}

'''num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

operador= input("operaor: + - * /\n  selecionene: ")

if operador == "+":
    print("la suma es " ,num1+num2)
elif operador == "-":
    print("la resta es " ,num1-num2)
elif operador == "*":
    print("la multiplicación es " ,num1*num2)
elif operador == "/":
    print("la división es " ,num1/num2)
'
# lista=[1,2,3,4,5]
# print(type(lista))
# print(lista)
# #convertirla en set
# lista_set=set(lista)
# print(lista_set)
# print(type(lista_set))
# #convetir en tupla
# lista_tupla=tuple(lista)
# print(lista_tupla)
# print(type(lista_tupla))

# print(sum(lista))
# print(max(lista))
# print(range(8))
# print(round(3.1416,2))

# infous = {
#     "nombre": "juan"
# }
# print(infous)
'''

#Exercise:

#1.

lista = [1, 2, 3, 4, 5]
print(f"El mínimo es: {min(lista)}")
print(f"El máximo es: {max(lista)}")
print(f"La suma del mínimo y el máximo es: {max(lista) + min(lista)}")

#2

coment = "Hola aprendices"
num = "de la ficha #3407184"
print (coment + " " + num)

#3

decimal1 = float(input("ingrese el primer numero decimal: "))
decimal2 = float(input("ingrese el segundo numero decimal: "))
suma_decimales = (decimal1 - int(decimal1)) + (decimal2 - int(decimal2))

print(f"los decimales son: {decimal1 - int(decimal1)} y {decimal2 - int(decimal2)} y su suma es: {suma_decimales}")

#4
radiocir = float(input("ingrese el radio de la circunferencia: "))
perimetro = 2 * 3.1416 * radiocir
area = 3.1416 * radiocir**2
print(f"Para una circunferencia con radio {radiocir}, el perimetro es {perimetro} y el area es {area}")

#5
numx = int(input("ingrese un numero: "))
if numx % 2 == 0:
    print(f"el numero {numx} es par")
else:    
    print(f"el numero {numx} es impar")
    
#6
nota1=int(input("ingrese la primera nota 1-10: "))
nota2=int(input("ingrese la segunda nota 1-10: "))
nota3=int(input("ingrese la tercera nota 1-10: "))

promaritmetico = (nota1 + nota2 + nota3) / 3
if promaritmetico >= 7.8:
    print(f"aprobo con {round(promaritmetico, 2)}")
else:
    print(f"reprobo con {round(promaritmetico, 2)}")
    
#7
prepro = int(input("ingrese el precio del producto: "))
if prepro > 120000:
    des = 0.15
    predes = prepro * des
    prefinal = prepro - predes
    print(f"El precio final con descuento es: {prefinal}")
else:
    print(f"El precio final es: {prepro}")
    
#8
name = (input("Write the name: "))
age = int(input("Write your age: "))
if age >= 18:
    print(f"Welcome {name}")
else: 
    print(f"Sorry, the min age is 18 years old, you have {age} years old.")
#1

hour = int(input("Write the hour: 8am ,10am ,12pm ,3pm ,7pm"))
match hour:
    case 8:
        print("Hora del desayuno")
    case 10:
        print("Hora medias nueves")
    case 12:
        print("Hora de almuerzo")
    case 15:
        print("Hora de las onces")
    case 19:
        print("Hora de la cena")
    case _:
        print("Invalid hour")

#2

while True:
    day = int(input("write the day 1 to 7:  "))
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
            break
        case _:
            print("Invalid day number. Please enter a number between 1 and 7.")

#3          
Name = (input("Write your name"))
Estrato = (input("Write your stratum: 1,2,3,4,5,6"))

match Estrato:
    case "1":
        print(f"{Name} you are stratum{Estrato} and you have subsidy ")
    case "2":
        print(f"{Name} you are stratum{Estrato} and you have subsidy")
    case "3":
        print(f"{Name} you are stratum{Estrato} and you have subsidy")
    case "4":
        print(f"{Name} you are stratum{Estrato} and you no have ")
    case "5":
        print(f"{Name} you are stratum{Estrato} and you no have ")
    case "6":
        print(f"{Name} you are stratum{Estrato} and you no have ")
    case _:
        print("Invalid stratum. Please enter a number between 1 and 6.")
        
#4
month = int(input("Write the month number: 1 to 12: "))
match month:
    case 1 | 2 | 3: #comodines
        print("The season is: Summer")
    case 4 | 5 | 6:
        print("The season is: Autumn")
    case 7 | 8 | 9:
        print("The season is: Winter")
    case 10 | 11 | 12:
        print("The season is: Spring")
    case _:
        print("Invalid month number. Please enter a number between 1 and 12.")
        
#5
lado1 = float(input("ingrese el lado 1 del triangulo: "))
lado2 = float(input("ingrese el lado 2 del triangulo: "))
lado3 = float(input("ingrese el lado 3 del triangulo: "))
match (lado1, lado2, lado3):
    case (lado1, lado2, lado3) if lado1 == lado2 == lado3:
        print("El triángulo es equilátero")
    case (lado1, lado2, lado3) if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles")
    case (lado1, lado2, lado3) if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("El triángulo es escaleno")
    case _:
        print("Los lados ingresados no forman un triángulo válido.")
        
#6
prepro = int(input("ingrese el precio del producto: "))
match prepro:
    case prepro if prepro >= 100000:
        des= 0,85
        prefi = prepro * des
        print(f"El precio final con descuento es: {prefi}")
        
    case prepro if prepro >= 180000:
        des= 0,80
        prefi = prepro * des
        print(f"El precio final con descuento es: {prefi}")
        
    case prepro if prepro >= 250000:
        des= 0,75
        prefi = prepro * des
        print(f"El precio final con descuento es: {prefi}")
        
    case prepro if prepro >= 400000:
        des= 0,70
        prefi = prepro * des
        print(f"El precio final con descuento es: {prefi}")
        
    case _:
        
        print(f"No cuenta con descuento, El precio final es: {prepro}")
        
#Sangria = espacios que se dejan o en termino programacion indentacion.