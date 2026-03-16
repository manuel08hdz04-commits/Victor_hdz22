#Métodos y funciones de los diccionarios
#Metodo keys():El método retorna o regresa una lista de todas las claves
#dentro del diccionario. Al tener una lista de claves se
#puede acceder a todo el diccionario de una manera fácil y útil.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

#Función sorted()
#Values()
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for french in dictionary.values():
    print(french)

#Agregar una nueva clave
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)

#Eliminar una clave
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary['perro']
print(dictionary)

#Metodo popitem(): Elimina el ultimo elemento de la lista
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.popitem()
print(dictionary)    # salida: {'gato': 'chat', 'perro': 'chien'}

