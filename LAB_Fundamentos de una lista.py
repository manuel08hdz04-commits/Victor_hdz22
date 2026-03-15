#LAB_FUNDAMENTIOS DE UNA LISTA

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

num=int(input("Que numero reemplazara al número de en medio:"))# Paso 1: escribe una línea de código que solicite al usuario
hat_list[2] = num# reemplazar el número de en medio con un número entero ingresado por el usuario.

del hat_list[4]# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

print("Longitud de la nueva lista:", len(hat_list))# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print(hat_list)

#LAB   Los fundamentos de las listas: los Beatles


beatles=[]

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    nombre=input("Ingresa los miembros que faltan:")
    beatles.append(nombre)

print("Lista despues de agregar a los miembro", beatles)

del beatles[3]
del beatles[3]
print("Lista después de eliminar miembros:", beatles)

beatles.insert(0, "Ringo Starr")

print("Lista final de los Beatles:", beatles)
print("Número total de miembros:", len(beatles))
