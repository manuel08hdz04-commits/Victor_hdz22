#ALGORITMO BURBUJA
# lsr.sort() ordena elementos de una lista
#lst.reverse() invierte una lista

#Rebanada: crea una nueva lista de destino
#my_list[start:end]
#start es el índice del primer elemento incluido en la rebanada.
#end es el índice del primer elemento no incluido en la rebanada

#instrucciòn del puede eliminar rebanadas
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#Operadores para verificar si un elemento esta almacenado en la lista
#elem in my_list
#elem not in my_list
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#  LAB   Operaciones con listas: conceptos básicos
numeros = [1, 2, 3, 2, 4, 5, 3, 1, 6]
sin_repetidos = []

for num in numeros:
    if num not in sin_repetidos:
        sin_repetidos.append(num)

print("Lista sin repeticiones:", sin_repetidos)
