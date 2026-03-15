#Funciones:Una funcion es un bloque de codigo que realiza una tarea especifica cuando la
#la función es invocada, hace el codigo reutilizable
def message():
    print("Ingresar valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

#Funciones con parametros: Los parametros solo existen dentro de las funciones en donde han
#sido definidos
#la asignación de un valor a un parámetro de una función se hace en el momento
#en que la función se manda llamar o se invoca,
def message(what, number):
    print("Ingresa", what, "número", number)

message("teléfono", 11)
message("precio", 5)
message("número", "number")

#Paso por parametros posicionales
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

#Paso de argumentos por palabras clave
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introductio

#Mezclando argumentos posicionales y de palabras clave
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
    
adding(1, 2, 3)

