
#importan date

#pip install flask
#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hola_mundo():
#    return "Hola"

#if __name__ == '__main__':
#    app.run(debug=True)

#Exercice 1 print hello word
print("Hello word")
print("Hello \nword")

#print

mi_texto = "Hello Word "
miotro_texto = "Python is beautifull"
Mensaje_Final = mi_texto + miotro_texto
print(Mensaje_Final)
#Ejemplo mio: 
print(f"{mi_texto}, {miotro_texto}")
print(mi_texto[0:10])
print(miotro_texto[0:16])

#Other example
#Ejemplo del profesor:
print ("hola", mi_texto, "i love ", miotro_texto)

#Exercice 2 values, types and operators!

#Types
print(type(1))
print(type("a"))
print(type(1j))
print(type(True))
print(type(1.5))

#values and bool
a = 1
b = "b"
print(10 > 20)
print(10 < 20)
print(10 // 20)
print(10 / 20)
print(10 == 10)
print(2 + 3)
print(2 * 3)
print(2 - 3)
print(2 ** 3)

#bool whit and, not and or
#bool and
print(True and False)
print(True and True)

#bool not
print(not False and False)
print(not True and True)

#bool or 
print(True or False)
print(False or False)

#operations
num1 = (input("Digite el numero uno: "))
num2 = 2
sum = num1 + num2
print(f"la suma de los dos números es {sum}")

x = b = c = "Hello word"
print(x)

#list
my_list = list()
my_person = []
my_list = ["pedro",10,1.75,"1245jk","montes"]
my_person = ["miguel",17,1.75,"245jkl","miguel"]

print(len(my_list))
print(type(my_list))

print(len(my_person))
print(type(my_person))
print(my_person[0])
print(my_person.count("miguel"))
name, years, heigh, password, name = my_person
print(heigh)

lista = [
    [{"Andres","Gonzalez",16,},{"Luzmi","Cordoba",18}],
    [{"Daniel","Gonzalez",26},{"Yeison","Gonzalez",24}],
    [{"Mariela","Loaiza",59},{"Henry","Rodriguez",51}],
    [{"Camilo","Gonzalez",26},{"David","Gonzalez",24}],
]

print(lista[1][2]) 
    
print(len(lista[0][0]))
print(lista.count("Gonzalez"))
print(type(lista))

msg = lista[1][0]
print(msg)

print(my_list + my_person)

lista.append("sebastian")
print(lista)

lista.insert(1, "Sebastian")
print(lista)

lista.remove("sebastian")
print(lista)

lista = "Hello word"
print(lista)
print(type(lista))

print(my_person.pop())

my_newperson = my_person.copy()
print(my_newperson)

my_person.clear()
print(my_person)
print(my_newperson)

my_newperson.reverse()
print(my_newperson)

print(my_newperson.reverse())

num1 = [1,2,3,4,5,6,7,8,9,10,1,1,6,5,8,1]
num2 = [11,12,13,14,15,16,17,11,15,11,12]

num1.sort()
print(num1)

print(num1.count(1))
print(num1 + num2)

num1.insert(1, 30)
print(num1)  

print(num1[1:2])

del my_list

#list

mi_list = ["Andres","16"]
print(mi_list)
print(len(mi_list))
print(mi_list[0])
print(mi_list.count("Andres"))
name,years = mi_list
print(name)

#lista x2

lista = [
    [{"Andres",16,"Andres"},{"Luzmi",18}],
    [{"Daniel",26},{"Yeison",24}],
]
print(lista[0][1])
print(len(lista[0][1]))

print(my_list + lista)

lista.append("sebastian")
print(lista)

lista.insert(1, "Sebastian")
print(lista)

lista.remove("sebastian")
print(lista)
print(lista.pop())

my_newperson = my_list.copy()
print(my_newperson)

#Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (10,1.12,"Andres","Blue")
my_other_tuple = (35,60, 90)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Blue"))
print(my_tuple.index("Andres"))
print(my_tuple.index("Blue")) 
 
print(my_tuple + my_other_tuple)

my_sum = my_tuple + my_other_tuple
print(my_sum)

print(my_sum[3:5])
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple[3]= "Blue"
my_tuple.insert(1, "Red")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple

#sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Andres","Blue"}
print(type(my_other_set)) 

print(len(my_other_set))

my_other_set.add("luzmi") #No admite repetidos
print(my_other_set )

print("Andres" in my_other_set)
print("Alejo" in my_other_set)

my_other_set.remove("Andres")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set

my_set = {"Andres","luzmi"}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"name","gmail"}
my_new = my_set.union(my_other_set)
print(my_new.union(my_new).union(my_set).union({"javaScript", "C#"}))
print(my_new.difference(my_set))

#Dicctionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name": "Andres", "Years":15}

my_dict = {
    "Firsname":"luzmi",
    "lastname":"ayalen",
    "years":18,
    "lenguaje": {"python","php"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)
print(my_dict["lenguaje"])
my_dict["Firsname"] = "Andres"
print(my_dict["Firsname"])
print(my_dict[1])

my_dict["cod"] = 1
print(my_dict)

del my_dict["cod"]
print(my_dict)

print("ayalen" in my_dict)
print("lastname" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Firsname", 1, "Piso"]

my_new = dict.fromkeys(my_list)
print(my_new)
my_new = dict.fromkeys(my_list)
print("Firsname", 1, "Piso")
my_new = dict.fromkeys(my_list, ("Andres", "Gonzalez"))
print(my_new.values())
print(list(my_new))
print(set(my_new))
print(tuple(my_new))

#Conditionals

my_con = True

if my_con:
    print("Con if")

print("continue")

my_con = 5*2

if my_con == 11:
    print("The second print if")

print("number diferent")
 
if my_con >= 10:
    print("The second print if")
else:
    print("error")
my_con = 5*2

if my_con > 10 and my_con <20:
    print("higth 10 and low 20")
else:
    print("low 10 and hight 20")

my_con = 5*2
if my_con > 10 and my_con <20:
    print("higth 10 and low 20")
elif my_con == 1:
    print("igual 1")
else:
    print("low 10 and hight 20")

#Blucles/loops and cicles
#loops mecanisco de iteracion = repeticion

#While
my_condiction = 0
 
while my_condiction < 10:
    print(my_condiction)
    my_condiction += 1
else: #is optional
    print("Mi condicion es mayor o igual que 10")
#

while my_condiction < 20:
    my_condiction  += 1
    if my_condiction == 15:
        print("Se detiene la ejecucion")
        break
    print(my_condiction)

#for iteracion de estado de elementos se usa en listas
my_list = [1, 2, 3, 4]

for element in my_list:
    print(element)


for element in my_dict:
    print(element)
    if element == "years":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

for element in my_dict:
    print(element)
    if element == "years":
        continue
    else:
        print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

for element in list(my_dict.values()):
    print(element)
user = {
    "Alejandro":"123"
}
username = str(input("Username: "))
password = input("Password: ")

if username in user and user[username] == password:
    print(f"Hello {username}")
else:
    print("incorrect Username or Password")

#functions

"def my_function ():"


#class    
    
class person:
    def __init__(self, name, years):
        
        self.name = name
        self.years = years
        
    def hello(self):
       print(f"Nice to meet you {mi_person.name}")
        
mi_person = person ("Alejandro", "18")

print(f"Hello mi name is {mi_person.name}")
print(f"i am {mi_person.years} years old")

mi_person.hello()

#class execises:

class person:
    def __init__(self, name, years):
        
        self.name = name
        self.years = years
        
    def hello(self):
       print(f"Nice to meet you {mi_person.name}")
        
mi_person = person ("Alejandro", "18")

print(f"Hello mi name is {mi_person.name}")
print(f"i am {mi_person.years} years old")

mi_person.hello()

class calculadora:
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
        self.Resultado = 0

    def sumar(self):
        self.Resultado = self.Num1 + self.Num2
        return self.Resultado
    
    def resta(self):
        self.Resultado = self.Num1 - self.Num2
        return self.Resultado
    
    def division(self):
        self.Resultado = self.Num1 / self.Num2
        return self.Resultado
    
    def multiplicacion(self):
        self.Resultado = self.Num1 * self.Num2
        return self.Resultado
    
    def potenciacion(self):
        self.Resultado = self.Num1 ** self.Num2
        return self.Resultado

mi_calcu = calculadora(15, 10)
print(mi_calcu.sumar())
print(mi_calcu.resta())
print(mi_calcu.division())
print(mi_calcu.multiplicacion())
print(mi_calcu.potenciacion())

class perso:
    def __init__(self,name,nacimiento,actual):
        self.name = name
        self.nacimiento = nacimiento
        self.actual = actual
        self.years = 0 
    
    def hello(self):
        self.years = self.actual - self.nacimiento
        return self.years
     
my_perso = perso ("Sebastian",2008,2025)
print(f"hello {my_perso.name}")
print(f"i have {my_perso.hello()} years old")
    
#Quiz 

test =[ 
    {"message":"Wrong"},   
    {"array":[
            [{},],
            [{"message":{"hi":["Hello"]}}]]
    },
    {"wrong":["value"]}
] 

msg = test[1]["array"][1][0]["message"]["hi"][0]
print(msg)











#future code import class turtle

import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(100)
t.pensize(1)
h = 0.5
for i in range(250):
    c= colorsys.hsv_to_rgb(h,1,1)
    h= 0.0008
    t.fillcolor(c)
    t.begin_fill()
    t.fd(i)
    t.lt(100)
    t.circle(30)
    for j in range(2):
        t.fd(i*j)
        t.rt(109)
    t.end_fill()
    

import turtle as tur
import colorsys as cs 
tur.setup(800,800)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor("black")
for j in range (25):
    for i in range (15):
        tur.color(cs.hsv_to_rgb(i/15,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
tur.hideturtle()
tur

#cases and while
conunt = {}
"""
while True:
    log = input("Enter the option: 1 = Login, 2 = Register, 3 = Exit: ")

    match log:
        case "1":
            print("Login")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in conunt and conunt[username] == password:
                print("Login successful!")

                while True:
                    print(f"\nHello {username}")
                    print("\n--- Menu ---")
                    print("1 = Catalog")
                    print("2 = Cart")
                    print("3 = Waiting time")
                    print("4 = Config account")
                    print("5 = Close account")

                    menu_option = input("Enter the option: ")

                    match menu_option:
                        case "1":
                            print("")
                        case "2":
                            print("")
                        case "3":
                            print("")
                        case "4":
                            while True:
                                print("\n--- Config Menu ---")
                                print("1 = Phone number")
                                print("2 = User settings")
                                print("3 = Credit card")
                                print("4 = Privacy")
                                print("5 = Back")

                                opc = input("Enter the option: ")

                                match opc:
                                    case "1":
                                         while True:
                                            print("\n--- Phone number options ---:")
                                            print("1 = Delete")
                                            print("2 = Update")
                                            print("3 = Add new number")
                                            print("4 = Back")

                                            opcn = input("Enter the option: ")

                                            match opcn:
                                                case "1":
                                                    print("\n--- Delete phone number ---")
                                                    delete = input("Are you shure 1= del, 2= return: ")
                                                    match delete:
                                                        case "1":
                                                            print("Success. Phone number deleted.")
                                                        case "2":
                                                            print("return to menu config...")
                                                            break
                                                case "2":
                                                    print("\n--- Update phone number ---")
                                                    new = input("Enter the new number: ")
                                                    print(f"Success, phone number updated: {new}")
                                                case "3":
                                                    print("\n--- Add new phone number ---")
                                                    new = input("Enter the new phone number: ")
                                                    print(f"Success, new phone number: {new}")
                                                case "4":
                                                    break
                                                case _:
                                                    print("Invalid option.")

                                    case "2":
                                        while True:
                                            print("\n--- User options ---")
                                            print("1 = Change username")
                                            print("2 = Change profile photo")
                                            print("3 = Back")

                                            opcu = input("Enter the option: ")

                                            match opcu:
                                                case "1":
                                                    nom = input("Enter new username: ")
                                                    print(f"Success, new username is {nom}")
                                                case "2":
                                                    print("Photo selected successfully.")
                                                case "3":
                                                    break
                                                case _:
                                                    print("Invalid option.")

                                    case "3":
                                         while True:
                                            print("\n--- Credit Card ---")
                                            print("1 = Credit card info")
                                            print("2 = Add new credit card")
                                            print("3 = Back")
                                        
                                            opcu = input("Enter the option: ")

                                            match opcu:
                                                case "1":
                                                    nom = input("Enter new username: ")
                                                    print(f"Success, new username is {nom}")
                                                case "2":
                                                    print("Photo selected successfully.")
                                                case "3":
                                                    break
                                                case _:
                                                    print("Invalid option.")


                                    case "4":
                                        print("Privacy settings updated.")

                                    case "5":
                                        break

                                    case _:
                                        print("Invalid option.")

                        case "5":
                            print("Account closed. Logging out...")
                            break

                        case _:
                            print("Invalid option.")

            else:
                print("Invalid username or password.")

        case "2":
            print("Register")
            new_user = input("Enter new username: ")

            if new_user in conunt:
                print("That username already exists. Try another one.")
            else:
                new_phonenumber = input("Enter phone number: ")
                new_email = input("Enter the email: ")
                new_pass = input("Enter the password: ")
                conunt[new_user] = new_pass
                print(f"User '{new_user}' registered successfully.")

        case "3":
            print("Goodbye!")
            break

        case _:
            print("Invalid option.")

#web

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def operar():
    resultado = None
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        resultado = num1 + num2

    return f'''
        <html>
        <head>
            <title>Operación en Flask</title>
        </head>
        <body>
            <h1>Sumar dos números</h1>
            <form method="POST">
                Número 1: <input type="number" name="num1"><br><br>
                Número 2: <input type="number" name="num2"><br><br>
                <input type="submit" value="Sumar">
            </form>
            {f"<h2>Resultado: {resultado}</h2>" if resultado is not None else ""}
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
"""

#Exercise in class at SENA
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