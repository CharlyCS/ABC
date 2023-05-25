import pymysql
from flask import Flask
from flask import Flask, render_template, request, redirect, flash

import controlador_users
import controlador_usuarios
import controlador_documentos

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='1234',
                                db='uni')
    
app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('register.html')

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('login.html')

@app.route("/register", methods=["POST"])
def register():
   
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    controlador_users.registrar_usuario( username,password,email)
    # De cualquier modo, y si todo fue bien, redireccionar
  
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    
    username = request.form["username"]
   
    password = request.form["password"]
    sesion=controlador_users.login_usuario( username,password)
    # De cualquier modo, y si todo fue bien, redireccionar
    if sesion:
        x = controlador_documentos.obtener_documento()
        return render_template("documentos.html",documentos=x)
    else:
        return "El usuario no existe"
#############################
#############################
@app.route("/documentos")
def documentos():
    x = controlador_documentos.obtener_documento()
    return render_template("documentos.html",documentos=x)

@app.route("/usuarios")
def usuarios():
    x = controlador_usuarios.obtener_alumnos()
    return render_template("usuarios.html",usuarios=x)
#############################
#############################
@app.route("/agregar_documento") #/URL que sale
def formulario_agregar_documento(): #definicion de funcion
    return render_template("agregar_documento.html")

@app.route("/agregar_usuario")
def formulario_agregar_usuario():
    return render_template("agregar_usuario.html")
#############################
#############################
@app.route("/formulario_editar_documento/<int:id>")
def editar_documento(id):
    # Obtener el juego por ID
    x = controlador_documentos.obtener_documento_por_id(id)
    return render_template("editar_documento.html", documento=x)

@app.route("/formulario_editar_usuario/<int:id>")
def editar_usuario(id):
    # Obtener el juego por ID
    x = controlador_usuarios.obtener_alumno_por_id(id)
    return render_template("editar_usuario.html", usuario=x)
#############################
#############################
@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    idUsuario = request.form["idUsuario"]
    nombre = request.form["nombre"]
    apellidos = request.form["apellidos"]
    correo = request.form["correo"]
    celular = request.form["celular"]
    rol = request.form["rol"]
    contraseña = request.form["contraseña"]
    controlador_usuarios.insertar_alumno(idUsuario, nombre, apellidos , correo, celular, rol, contraseña)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/usuarios")
    
@app.route("/guardar_documentos", methods=["POST"])
def guardar_documento():
    idDoc = request.form["idDocumento"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    categoria = request.form["categoria"]
    nose = request.form["nose"]
    controlador_documentos.insertar_documento(idDoc, nombre, descripcion , categoria, nose)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/documentos")
#############################
#############################
@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    id = request.form["idUsuario"]
    #idAlumno = request.form["idAlumno"]
    nombre = request.form["nombre"]
    apellidos = request.form["apellidos"]
    correo = request.form["correo"]
    celular = request.form["celular"]
    rol = request.form["rol"]
    contraseña = request.form["contraseña"]
    controlador_usuarios.actualizar_alumno(nombre, apellidos , correo, celular, rol, contraseña, id)
    return redirect("/usuarios")
#@app.route("/for")

@app.route("/actualizar_documento", methods=["POST"])
def actualizar_documento():
    id = request.form["idDocumento"]
    #idAlumno = request.form["idAlumno"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    categoria = request.form["categoria"]
    nose = request.form["nose"]
    #precio = request.form["precio"]
    controlador_documentos.actualizar_documento(nombre, descripcion , categoria, nose, id)
    return redirect("/documentos")
#@app.route("/for")


#############################
#############################
@app.route("/eliminar_documento", methods=["POST"])
def eliminar_documento():
    controlador_documentos.eliminar_documento(request.form["idDocumento"])
    return redirect("/documentos")

@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    controlador_usuarios.eliminar_alumno(request.form["idUsuario"])
    return redirect("/usuarios")


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)