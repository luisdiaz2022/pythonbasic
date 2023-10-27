# Funciones

def miFuncion():
    print('Mi primera funcion!')

# miFuncion()

def imprimeDato(*nombre): # argumento que recibe la funcion # * nos permite pasar varios parametros, obtenemos tupla
    print('Mi argumento es', nombre[1])

# imprimeDato('Chanchito', 'Feliz') # parametro que pasamos a la funcion

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='Chanchito', apellido='feliz') # asignamos el valor al argumento de la funcion, no orden especifico

def nombreCompleto2(**kwargs): # permite acceder a los argumentos usando la sintaxis de diccionario
    print(kwargs['nombre'], kwargs['apellido'])

# nombreCompleto(nombre='Chanchito', apellido='feliz')

def miFuncion2(argumento = 'Chanchito'): #
    print(argumento)

# miFuncion2('Batman')
# miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['Chanchito', 'Feliz'])

def concatenaNombres(lista):
    i = '' # string vacio
    for el in lista:
        i = i + el + ' '
    return i

# nombres = concatenaNombres(['Chanchito', 'Feliz'])
# print(nombres)

def recursion(i):
    if( i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)