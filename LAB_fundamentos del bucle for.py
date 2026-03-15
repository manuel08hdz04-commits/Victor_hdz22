#LAB_Fundamentos del bucle for – contando lentamente (mississippily)
cuenta=1
for i in range(5):
    print(cuenta,"Mississippi")
    cuenta += 1
#Uso de import time
import time

cuenta=1
for i in range (5):# Escribe un bucle for que cuente hasta cinco.
    print(cuenta,"Mississippi")# Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    cuenta+=1
    time.sleep(1)# Cuerpo del bucle, emplea : time.sleep(1)

print("Lista o no, aquí vengo!")# Escribe una función print con el mensaje final.

#Sentencias Break y continue
#Break: sale del bucle inmediatamente e incondicionalmente
#continue: e comporta como si el programa hubiera llegado repentinamente
#al final del cuerpo; el siguiente turno se inicia
#y la expresión de condición se prueba de inmediato.

#LAB_La sentencia break - atrapado en un bucle

Palabra_secreta="chupacabra"


while Palabra_secreta =="chupacabra":
    palabra=input("Ingresa la palabra secreta:")
    if palabra==Palabra_secreta:
        print("Has dejado el bucle con éxito.")
        break

# LAB   La sentencia continue – el Feo Devorador de Vocales

user_word=input("Ingrese una palabra:")

user_word=user_word.upper()

for letra in user_word:
    if letra =="A":
        continue
    elif letra =="E":
        continue
    elif letra =="I":
        continue
    elif letra =="O":
        continue
    elif letra=="U":
        continue
    print(letra)

