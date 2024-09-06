"""
Autores:
Nombre: Joseph Piñar Baltodano
ID: 1 1890 0308

Nombre: Abigail Salas Ramírez
ID: 4 0257 0890

Nombre: Gianpablo Moreno Castro
ID: 4 0261 0240
"""
from flask import Flask, jsonify, render_template
from database import Database
import pandas as pd

app = Flask(__name__)  # Inicialización de la aplicación Flask
db = Database()  # Instancia de la clase `Database` para conectarse a la base de datos

"""
Este archivo implementa un servidor web utilizando Flask. El servidor ofrece varias rutas
para acceder a la información relacionada con el rendimiento de la base de datos, 
como la tasa de hit del buffer caché, el estado de los tablespaces y las bitácoras (redo logs).
"""

@app.route('/')
def index():
    """
    Ruta de inicio que devuelve la página principal.
    Renderiza el archivo HTML `index.html` como respuesta al acceder a la raíz del servidor.
    """
    return render_template('index.html')

@app.route('/data')
def get_data():
    """
    Esta ruta realiza las siguientes operaciones:
    1. Recolecta datos sobre la tasa de hits, las lecturas físicas y las lecturas lógicas.
    2. Los datos recolectados se organizan en un DataFrame de Pandas.
    3. Devuelve los datos en formato JSON.
    """
    db.establecer_conexion()  # Establecer la conexión con la base de datos
    tasa_hit = []
    lecturas_fisicas = []
    lecturas_logicas = []
    
    # Se recolectan los datos de la base de datos en múltiples iteraciones
    for x in range(5):
        tasa_hit.append(db.tasa_de_hit())  # Obtener la tasa de hits
        lecturas_fisicas.append(db.total_lecturas_fisicas())  # Obtener lecturas físicas
        lecturas_logicas.append(db.total_lecturas_logicas())  # Obtener lecturas lógicas

        # Estructura de datos que se va a convertir en DataFrame
        data = {
            'tasa_hits': tasa_hit,
            'lecturas_fisicas': lecturas_fisicas,
            'lecturas_logicas': lecturas_logicas
        }
    
    # Crear un DataFrame a partir de los datos recolectados
    df = pd.DataFrame(data=data, columns=['tasa_hits', 'lecturas_fisicas', 'lecturas_logicas'])
    
    # Retornar el DataFrame en formato JSON
    return df.to_json()

@app.route('/tablespaces')
def get_tablespaces():
    """
    Ruta que devuelve información sobre los tablespaces de la base de datos.

    1. Obtiene la información de los tablespaces a través del método `calculo_tablespaces`.
    2. Devuelve los datos en formato JSON.
    """
    db.establecer_conexion()  # Establecer la conexión con la base de datos
    info_tablespaces = db.calculo_tablespaces()  # Obtener información sobre los tablespaces
    return info_tablespaces.to_json()  # Retornar los datos en formato JSON

@app.route('/bitacoras')
def get_bitacoras():
    """
    Ruta que proporciona información sobre las bitácoras (redo logs) de la base de datos.
    1. Obtiene la información de las bitácoras a través del método `bitacoras`.
    2. Devuelve los datos en formato JSON.
    """
    db.establecer_conexion()  # Establecer la conexión con la base de datos
    info_bitacoras = db.bitacoras()  # Obtener información sobre las bitácoras (redo logs)
    return info_bitacoras.to_json()  # Retornar los datos en formato JSON

if __name__ == '__main__':
    """
    Inicia el servidor Flask en modo de depuración (debug=True) en el puerto 5000.
    """
    app.run(debug=True, port=5000)
