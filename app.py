import time
from flask import Flask, jsonify, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
from database import Database

app = Flask(__name__)

"""Crear un dataset en donde el eje x sean los segundos
y el eje y el porcentaje del 1 al 100 con respecto a la tasa
sería bueno compartir un punto en específico.
Hay que investigar bien cómo se crea un dataframe para tres líneas y que hagan match en los datos de los ejes
Por el sueño no sé si sea necesario, ya que en el gráfico se ven los porcentajes y abajo se ve la cantidad total"""

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data')
def get_data():
    db = Database()
    db.establecer_conexion()
    tasa_hit = db.tasa_de_hit()
    lecturas_fisicas = db.total_lecturas_fisicas()
    lecturas_logicas = db.total_lecturas_logicas()
    data = [{
        "fecha" : time.time(),
        "tasa_hit" : tasa_hit,
        "lecturas_fisicas" : lecturas_fisicas,
        "lecturas_logicas" : lecturas_logicas,
    }]
    #df = pd.DataFrame(data, columns=['fecha', 'tasa_hit', 'lecturas_fisicas', 'lecturas_logicas'])
    #result = df.to_dict(orient='records')
    return jsonify(data)


@app.route('/ping')
def ping():
    return '<p>pong</p>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)