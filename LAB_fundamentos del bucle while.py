#LAB_Fundamentos del bucle while
blocks = int(input("Ingresa el número de bloques: "))

height = 0
layer = 1

while blocks >= layer:
    blocks = blocks - layer
    height += 1
    layer += 1

print("La altura de la pirámide es:", height)

#LAB   La hipótesis de Collatz
c0 = int(input("Ingresa un número natural: "))

steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    
    print(c0)
    steps += 1

print("Número total de pasos:", steps)
