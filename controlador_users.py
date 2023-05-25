import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='1234',
                                db='uni')


def registrar_usuario(username, password,email):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO users(username, password,email) VALUES ( %s, %s, %s)",
                       (username, password, email))
    conexion.commit()
    conexion.close()
    
def login_usuario( username, password):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    return user
    
    
