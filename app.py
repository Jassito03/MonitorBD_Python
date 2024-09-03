import time
from flask import Flask, jsonify, render_template
from database import Database
import pandas as pd

app = Flask(__name__)
db = Database()

"""Crear un dataset en donde el eje x sean los segundos
y el eje y el porcentaje del 1 al 100 con respecto a la tasa
sería bueno compartir un punto en específico.
Hay que investigar bien cómo se crea un dataframe para tres líneas y que hagan match en los datos de los ejes
Por el sueño no sé si sea necesario, ya que en el gráfico se ven los porcentajes y abajo se ve la cantidad total"""

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


@app.route('/ping')
def ping():
    return '<p>pong</p>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)