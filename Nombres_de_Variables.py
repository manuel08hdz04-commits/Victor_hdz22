#Cajas con forma de Datos
#Palabras Clave Reservadas
'''['False', 'None', 'True', 'and', 'as', 'assert',
'break', 'class', 'continue', 'def', 'del',
'elif', 'else', 'except', 'finally', 'for',
'from', 'global', 'if', 'import', 'in', 'is',
'lambda', 'nonlocal', 'not', 'or', 'pass',
'raise', 'return', 'try', 'while', 'with', 'yield']'''

var = 22
print(var)
var = var + 1
print(var)

Nombre="Victor"
Apellido="Hernandez"
print("ING."+Nombre," "+Apellido)

#LAB_Variables
john=3
mary=5
adam=6
print(john,mary,adam,sep=",")
total_apples=john+mary+adam
print("Numero de manzanas:",total_apples)

#Operadores Abreviados
i+=2*j  #i=i+2*j
var/=2  #var/=2
rem%=10 #rem=rem%10
j-=(i+var+rem) #j=j-(i+var+rem)
x**=2  #x=x**2

#Conversiones
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

#Sustituciòn de variables
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)



