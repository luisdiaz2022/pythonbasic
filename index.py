# aca va un comentario
# if 3 > 5: # aca va un comentario
    # print('esto no se va a imprimir')

# if 5 > 3: # aca va otro  comentario
# print('5 es mayor a 3')

x = 5
y = 'chanchitos felices'

# print(x, y)

email = 'chanchito@feliz.com'

# print(email)

mi_var = 'chanchito'

a, b, c = 'Lala', 'lele', 'lili'

# print(a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'

# print(valor1, valor2, valor3)

inicio = 'Hola'
final = 'Mundo'

# print(inicio + final)

palabra = 'hola mundo' # string
oracion = "hola mundo comilla doble" # string

entero = 20 # int
decimal = 20.2 # float
complejo = 1j # numero complejo

# print(palabra, oracion, entero, decimal, complejo)

lista = ['Hola', 'Mundo', 'Chanchito Feliz']
lista2 = lista.copy()
lista.append('Chanchito triste') # agregar elementos a la lista
# lista.clear() # limpia la lista

# print(lista, lista2.count(3)) #cuenta cuantas veces se repite un mismo elemento
# print(len(lista), len(lista2)) # cuantos elementos hay en toda la lista
largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista, largoLista2)

# print(lista[2])

# lista.pop() elimina el ultimo de la lista
# lista.remove('Hola') elimina elemento specifico por su valor

# lista.reverse() gira la lista
# lista.sort() organiza listas pero tienen que tener el mismo tipo de dato

# tupla (una lista que no se modifica) tiene menos metodos que las listas
tupla = ('Hola', 'Mundo', 'Somos', 'Tupla')
listaDeTupla = list(tupla) # adquirimos los datos de la tupla como una lista (podemos modificar la nueva lista)
listaDeTupla.append('chanchito')
# print(listaDeTupla)

rango = range(6) # importante para trabajar con iteraciones
# print(rango)

diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
} # coleccion de elementos con una key y un value

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])
# print(diccionario.get('nombre'))
diccionario['nombre'] = 'Fluffy'

# print(len(diccionario)) # podemos usar len en diccionarios

diccionario['ronronea'] = 'Si' # agrega key y su value

# print(diccionario)
# diccionario.pop('ronronea') # elimina key y su value
# print(diccionario)

# diccionario.popitem() #elimina el ultimo key que se agrego
# del diccionario['ronronea'] # elimina key y su value
# copiaGatito = diccionario.copy() # copia diccionario
# copiaGatito = dict(diccionario) # copia diccionario
# diccionario.clear() # Limpia todos los elementos del diccionario
# print(diccionario, copiaGatito)

fluffy = {
    "nombre": "Fluffy",
    "edad": 4,
}
mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}
gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}
print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6) # Crea Diccionario
print(perritos)

verdadero = True
falso = False

print(verdadero, falso)