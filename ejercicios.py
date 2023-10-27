# Primer ejercicio
# Un arreglo que va a conterner una lista de opciones - input y primer juego

# dato = input('ingrese dato: ')

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
#     print('El dato existe:', dato)
# else:
#     print('Ek dato no existe :(', dato)

# Ejercicio 2 Calculadora que suma

primero = input('Primer numero: ')
try: #intenta un proceso
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Primer numero: ')
try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('ingrese operacion: ')
if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '*':
    print('Multiplicacion: ', primero * segundo)
elif simbolo == '/':
    print('Division: ', primero / segundo)
else:
    print('El simbolo ingresado no es valido')

