from flask import Flask, render_template, request, redirect, jsonify, session
from flask_session import Session
import psycopg2
import bcrypt
import os
from pymongo import MongoClient

app = Flask(__name__)

# Configuración de la extensión Flask-Session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configuración de la base de datos PostgreSQL
postgres_connection = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost'
}

# Configuración de la base de datos MongoDB
mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['registro']
mongo_collection = mongo_db['archivos_pdf']



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/documentacion')
def documentacion():
    return render_template('documentacion.html')

@app.route('/infoPersonal')
def infoPersonal():
    return render_template('informacion-personal.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/verificar')
def verificar():
    return render_template('html/verificar.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos del formulario
    email = request.form['email']
    contraseña = request.form['contraseña']

    # Consultar en PostgreSQL si el usuario y la contraseña están registrados
    try:
        connection = psycopg2.connect(**postgres_connection)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM registro WHERE email=%s AND contraseña=%s', (email, contraseña))
        user_data = cursor.fetchone()
        connection.close()

        if user_data:
            # Los datos son correctos, redirigir a la página de inicio
            return redirect('/dashboard')
        else:
            # Los datos son incorrectos, mostrar un mensaje de alerta
            return render_template('login.html', error_message="Usuario o contraseña incorrectos")
    except psycopg2.Error as e:
        print(f"Error al consultar en PostgreSQL: {e}")
        # Mostrar un mensaje de alerta en caso de error en la consulta
        return render_template('login.html', error_message="Error en el servidor")


@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    # Obtener los datos del formulario
    num_identificacion = request.form['num_identificacion']
    nombres = request.form['nombres']
    apellido_paterno = request.form['apellido_paterno']
    apellido_materno = request.form['apellido_materno']
    email = request.form['email']
    contraseña = request.form['contraseña']
    

    # Guardar en PostgreSQL
    try:
        connection = psycopg2.connect(**postgres_connection)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO registro (num_identificacion, nombres, apellido_paterno, apellido_materno, email, contraseña ) VALUES (%s, %s, %s, %s, %s, %s)', (num_identificacion, nombres, apellido_paterno, apellido_materno, email, contraseña))
        connection.commit()
        connection.close()
    except psycopg2.Error as e:
        print(f"Error al insertar en PostgreSQL: {e}")

    # Guardar en MongoDB
    # try:
    #     mongo_collection.insert_one({'usuario': usuario, 'constraseña': contraseña})
    # except Exception as e:
    #     print(f"Error al insertar en MongoDB: {e}")

    return redirect('/')



@app.route('/upload', methods=['POST'])
def upload():
    if 'cv' in request.files:
        cv_file = request.files['cv']
        save_file_to_mongodb(cv_file)

    if 'icedula' in request.files:
        icedula_file = request.files['icedula']
        save_file_to_mongodb(icedula_file)

    if 'cvotacion' in request.files:
        icedula_file = request.files['cvotacion']
        save_file_to_mongodb(icedula_file)

    if 'cacademico' in request.files:
        icedula_file = request.files['cacademico']
        save_file_to_mongodb(icedula_file)

    if 'claboral' in request.files:
        icedula_file = request.files['claboral']
        save_file_to_mongodb(icedula_file)

    if 'ilegal' in request.files:
        icedula_file = request.files['ilegal']
        save_file_to_mongodb(icedula_file)

    if 'noResponsabilidades' in request.files:
        icedula_file = request.files['noResponsabilidades']
        save_file_to_mongodb(icedula_file)

    if 'celaboral' in request.files:
        icedula_file = request.files['celaboral']
        save_file_to_mongodb(icedula_file)

    # Repeat the same process for other file inputs (cvotacion, cacademico, claboral, ilegal, celaboral, etc.)

    return redirect('/documentacion')


def save_file_to_mongodb(file):
    try:
        # Read the file data
        file_data = file.read()
        # Get the file name
        file_name = file.filename
        # Save the file to MongoDB
        mongo_collection.insert_one({'file_name': file_name, 'file_data': file_data})
    except Exception as e:
        print(f"Error al insertar en MongoDB: {e}")



if __name__ == '__main__':
    app.run(debug=True)
