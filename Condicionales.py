#Variables preguntas y respuestas
#Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100,
#y True if n es mayor o igual que 100.
n = int(input("Ingresa un número: "))
print(n >= 100)

#Condiciones y ejecución condicional
#Condicional IF, IF-ELSE Y ELIF
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

numero_mas_grande=number1

if number2 >numero_mas_grande:
    numero_mas_grande=number2
    
if number3 >numero_mas_grande:
    numero_mas_grande=number3

print("El número mas grande es:",numero_mas_grande)
