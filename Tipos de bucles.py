#Bucles
#While True: Mientras se cumpla su condición se repitira la ejecución
while True:
    print("Estoy atrapado dentro de un bucle.")
    break

#While:
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#LAB Adivina el número secreto

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

number=int(input("Introduce un número:"))

if number==secret_number:
    print(secret_number, "¡Bien hecho, muggle! Eres libre ahora.")
    

while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number=int(input("Ingresa un número nuevamente:"))
    if number==secret_number:
        print(secret_number ,"¡Bien hecho, muggle! Eres libre ahora.")

#Bucle for: contador
i = 0
while i < 100:
    # do_something()
    i += 1
    
for i in range(100):
    # do_something()
    pass
#n este caso, el primer argumento determina el valor inicial (primero)
#de la variable de control.
#El último argumento muestra el primer valor que no se asignará a la variable de control.
for i in range(2, 8):
    print("El valor de i es", i)

#El primer argumento pasado a la función range() nos dice cual es el número de inicio
#de la secuencia (por lo tanto 2 en la output).
#El segundo argumento le dice a la función dónde detener la secuencia (la función genera números hasta el número indicado por el segundo argumento, pero no lo incluye). Finalmente, el tercer argumento indica el paso, que en realidad significa la diferencia entre cada número en la secuencia
#de números generados por la función.
for i in range(2, 8, 3):
    print("El valor de i es", i)

    
