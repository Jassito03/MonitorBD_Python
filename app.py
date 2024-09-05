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

app = Flask(__name__)
db = Database()

"""
Servidor

"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    db.establecer_conexion()
    tasa_hit = []
    lecturas_fisicas = []
    lecturas_logicas = []
    for x in range(5):
        tasa_hit.append(db.tasa_de_hit())
        lecturas_fisicas.append(db.total_lecturas_fisicas())
        lecturas_logicas.append(db.total_lecturas_logicas())

        data = {
            'tasa_hits': tasa_hit,
            'lecturas_fisicas': lecturas_fisicas,
            'lecturas_logicas': lecturas_logicas
        }
    df = pd.DataFrame(data=data, columns=['tasa_hits', 'lecturas_fisicas', 'lecturas_logicas'])
    return df.to_json()

@app.route('/tablespaces')
def get_tablespaces():
    db.establecer_conexion()
    info_tablespaces = db.calculo_tablespaces()
    return info_tablespaces.to_json()

@app.route('/estructura_fisica')
def get_estructura_fisica():
    db.establecer_conexion()
    info_estructura_fisica = db.estructura_fisica()
    return info_estructura_fisica.to_json()

@app.route('/ping')
def ping():
    return '<p>pong</p>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)