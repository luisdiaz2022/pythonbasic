# if 2 < 5:
#     print('2 es menor que 5')
# if 2 == 2:
#     print('2 es igual a 2')
# if 2 == 3:
#     print('2 es igual a 3')
# if 2 > 5:
#     print('2 es mayor a 5')
# if 5 > 2:
#     print('5 es mayor a 2')
# if 2 != 2:
#     print('2 es diferente a 2')
# if 3 != 2:
#     print('3 es diferente a 2')
# if 3 >= 2:
#     print('3 es mayor o igual a 2')
# if 3 <= 3:
#     print('3 es menor o igual a 2')

if 2 > 5:
    print('2 menor a 5')
elif 2 > 5:
    print('lalala')
elif 2 < 5:
    print('lelele')
else:
    print('yo me imprimo solo si todo lo anterior evalua en falso')

if 2 > 5:
    print('2 menor a 5')
else:
    print('yo me imprimo solo si todo lo anterior evalua en falso 2')

if 2 < 5: print('if de una sola linea') # para evaluaciones cortas

print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false')

if 2 < 5 and 3 > 2:
    print('ambas devuelven true')

if 2 < 5 and 3 < 2:
    print('hay una falsa, esto no se mostrata')

if 1 < 0 or 1 > 0:
    print('una de las condiciones devolvio true')