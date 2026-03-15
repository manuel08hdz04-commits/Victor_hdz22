#Introducción a Bucles
# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.
 
largest_number = max(number1, number2, number3)
 
# Imprime el resultado.
print("El número más grande es:", largest_number)

#ESPATIFILIO
name = input("Introduce el nombre de la flor: ")

if name == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
elif name == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No", name + "!")

#LAB_Inpuestos
ingreso = float(input("Introduce el ingreso anual: "))

if ingreso < 85528:
	tax = ingreso * 0.18 - 556.02
else:
	tax = (ingreso - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

#LAB Fundamentos de la sentencia If-elif-else
 año = int(input("Introduce un año: "))

if año < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if año % 4 != 0:
		print("Año Común")
	elif año % 100 != 0:
		print("Año Bisiesto")
	elif año % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
