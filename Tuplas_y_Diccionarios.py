#Tuplas y diccionarios
#Tuplas utilixzan parentesis
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

#
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

#len() acepta tuplas y regresa el numero de elementos contenidos
#el operador + puede unir tuplas
#el operador * puede multiplicar las tuplas, asi como las listas
#los operadores in y not in funcionan de la misma manera que en las listas.


#Diccionarios: No es una secuencia pero puede adaptarse facilmente y ademas es mutable
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#Busquedad de palabras en frances
dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")


 
    
