x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)


#Función Input()
print("Dime lo que deseas...")
anything= input()
print("Hmm..", anything,"...¿en serio?")

#Conversión de datos
a= float(input("Ingresa el valor de a:"))
b= float(input("Ingresa el valor de b:"))
print("El resultado de la suma es:",a+b)

#Operadores (+) y (*) para cadenas
#(+) Concatenaciòn
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

#(*) Operador de replicaciòn
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#funciòn string
a= float(input("Ingresa el valor de a:"))
b= float(input("Ingresa el valor de b:"))
print("El resultado de la suma es:"+(str(a+b)))

#LAB_Entradas y Salidas simples
a= float(input("Ingresa el valor de a:"))
b= float(input("Ingresa el valor de b:"))
print("El resultado de la suma es:",a+b)
print("\nEl resultado de la resta es:",a-b)
print("\nEl resultado de la multiplicación es:",a*b)
print("\nEl resultado de la Divición es:",a/b)
print("\n¡Eso es todo, amigos!")

#Tarea de Operadores y expresiones
x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

#Reloj
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')
