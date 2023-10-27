# archivos
# c = open('chanchito.txt', 'w') # accesamos el archivo de texto # r = read, a = append, w = write, x crea archivo

# print(c.read()) # imprime totalidad del archivo read()
# print(c.readline()) # imprime una linea del archivo readline()

# for x in c:
#     print(x)

# c.write('\nagregamos una nueva linea a nuestro archivo') # escribe al final del archivo

# c.close()

# x = open('chanchito.txt')

# print(x.read())

import os

if os.path.exists('chanchito.txt'): #verifica que existe ese archivo
    os.remove('chanchito.txt') #elimina archivo
else:
    print('El archivo no existe')

os.rmdir('') # elimina una carpeta