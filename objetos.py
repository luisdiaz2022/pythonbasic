# clase en python

class Usuario: # Clase, primera letra mayuscula .. instancias en minuscula
    def __init__(self, nombre, apellido): #self es la referencia cuando lo instanciamos // init se ejecuta siempre que instanciamos la clase
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self): # metodo de la clase
        print('Hola! mi nombre es', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola! Me llamo', self.nombre, 'Y soy administrador')



usuario = Usuario('Felipe', 'Feliz')

# usuario.saludo() # aplicando el metodo de la clase
# usuario.nombre = 'Chanchito'
# usuario.saludo()
# del usuario.nombre #borra propiedad de la instancia
# del usuario #borra la instancia

# admin = Admin('Super', 'Feliz')
# admin.saludo()
# admin.superSaludo()

# Herencia

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola soy un', self.tipo, ' y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): # extendemos la clase a pesar del init del padre
        Animal.__init__(self, nombre, onomatopeya) # traemos el init del padre, sin esto no se ejecuta el init del padre
        print('Hola, soy un gato extendido')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre,onomatopeya) # extendemos la clase con otro metodo
        print('instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()
