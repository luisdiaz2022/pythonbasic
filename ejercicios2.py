# 1. multiplicar dos números sin usar el símbolo de multiplicación
a = 4
b = 8
resultado = 0

for x in range(a):
    resultado += b

# print(resultado)

# 2. ingresar nombre y apellido e imprimirlo al reves
nombre = 'Luis'
apellido = 'Diaz'

concatenacion = nombre + ' ' + apellido

# print(concatenacion[::-1])

# 3. escribir una función que encuentre el elemento menor de una lista
lista = [1, 2, 5, 43, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

# print(menor)

# 4. escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calculaVolumen(6)
# print(resultado)

# 5. escribir una función que indique si el usuario es mayor de edad
def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)

resultado = esMayor(usuario)
resultado2 = esMayor(usuario2)

# print(resultado, resultado2)

# 6. escribir una función que indique si un número es par o impar
def esPar(n):
    return n % 2 == 0

resultadopar = esPar(10)
# print(resultadopar)

# 7. escribir una función que indique cuantas vocales tiene una palabra
palabra = 'ChanchItoFeliz'
vocales = 0

for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

# print(vocales)

# 8. escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados
# lista = []
# print('Ingrese numeros y para salir escribra "basta"')

# while True:
#     valor = input('Ingrese valor: ')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Dato invalido')
#             exit()

# resultado8 = 0
# for x in lista:
#     resultado8 += x

# print(resultado8)

# 9. escribir una función que reciba nombre y apellido y los vaya agregando a
# un archivo
def agregaNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombreAArchivo('Luis', 'Diaz')
agregaNombreAArchivo('Isa', 'Guerrero')