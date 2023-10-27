import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Accedo1810',
    database='prueba'
)

cursor = midb.cursor()

# listar datos
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

# limitar datos
# cursor.execute('select * from Usuario limit 1')
# resultado = cursor.fetchall()
# print(resultado)


# ver definicion de la tabla
# cursor.execute('show create table Usuario')

# insertar datos
# sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
# values = ('micorreo@correo.co.nz', 'nombreusuario', 45)

# actualizar datos
# sql = 'update Usuario set email = %s where id = %s'
# values = ('micorreo@correo.com', 7)
# cursor.execute(sql, values)

# midb.commit()

# print(cursor.rowcount)

# eliminar datos
# sql = 'delete from Usuario where id = %s'
# values = (4,)
# cursor.execute(sql, values)
# midb.commit()

