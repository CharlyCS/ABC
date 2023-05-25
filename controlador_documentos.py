import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='1234',
                                db='uni')


def insertar_documento(idDocumento, nombre, descripcion , categoria, nose):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO documentos(idDocumento, nombre, descripcion , categoria, nose) VALUES (%s, %s, %s, %s, %s)",
                       (idDocumento, nombre, descripcion , categoria, nose))
    conexion.commit()
    conexion.close()
    
    
def obtener_documento():
    conexion = obtener_conexion()
    alumnos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idDocumento, nombre, descripcion , categoria, nose FROM documentos")
        alumno = cursor.fetchall()
    conexion.close()
    return alumno


def obtener_documento_por_id(id):
    conexion = obtener_conexion()
    alumno = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idDocumento, nombre, descripcion , categoria, nose FROM documentos WHERE idDocumento = %s", (id,))
        alum = cursor.fetchone()
    conexion.close()
    return alum

def actualizar_documento(nombre, descripcion , categoria, nose, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE documentos SET  nombre = %s, descripcion = %s, categoria = %s, nose = %s  WHERE idDocumento = %s",
                       (nombre,descripcion , categoria, nose ,id))
    conexion.commit()
    conexion.close()



def eliminar_documento(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM documentos WHERE idDocumento = %s", (id,))
    conexion.commit()
    conexion.close()

