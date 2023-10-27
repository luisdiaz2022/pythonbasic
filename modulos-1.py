# import modulos # nos traemos todo lo que este en el modulo
# import modulos as xs # Cambiamos la manera que referenciamos el modulo
from modulos import saludo, mascotas # importamos especifico 
from camelcase import CamelCase

# print(mascotas)
# saludo('Nicolas')

c = CamelCase()
s = 'esta oracion necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)