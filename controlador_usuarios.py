
from bd import obtener_conexion


def insertar_alumno(idUsuario, nombre, apellidos , correo, celular, rol, contraseña):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(idUsuario, nombre, apellidos , correo, celular, rol, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (idUsuario, nombre, apellidos , correo, celular, rol, contraseña))
    conexion.commit()
    conexion.close()
    
    

def obtener_alumnos():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idUsuario, nombre, apellidos , correo, celular, rol, contraseña FROM usuarios")
        usuario = cursor.fetchall()
    conexion.close()
    return usuario


def obtener_alumno_por_id(id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idUsuario, nombre, apellidos , correo, celular, rol, contraseña FROM usuarios WHERE idUsuario = %s", (id,))
        user = cursor.fetchone()
    conexion.close()
    return user

def actualizar_alumno(nombre, apellidos , correo, celular, rol, contraseña, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET  nombre = %s, apellidos = %s, correo = %s, celular = %s, rol = %s, contraseña = %s  WHERE idUsuario = %s",
                       (nombre, apellidos , correo, celular, rol, contraseña ,id))
    conexion.commit()
    conexion.close()



def eliminar_alumno(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE idUsuario = %s", (id,))
    conexion.commit()
    conexion.close()

