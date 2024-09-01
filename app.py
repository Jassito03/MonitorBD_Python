from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly
import json

app = Flask(__name__)
"""Crear un dataset en donde el eje x sean los segundos
y el eje y el porcentaje del 1 al 100 con respecto a la tasa
sería bueno compartir un punto en específico.
Hay que investigar bien cómo se crea un dataframe para tres líneas y que hagan match en los datos de los ejes
Por el sueño no sé si sea necesario, ya que en el gráfico se ven los porcentajes y abajo se ve la cantidad total"""
@app.route('/')
def index():
    df = pd.DataFrame({
         "Porcentaje": [
        50,65,60,68,70,
        89,90,85,89,92,
        45,48,50,42,60
    ],
    "Segundos": [
        1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5
    ],
    "Categoría": [
        "Lectuas Físicas", "Lectuas Físicas", "Lectuas Físicas", "Lectuas Físicas", "Lectuas Físicas",
        "Lecturas lógicas","Lecturas lógicas", "Lecturas lógicas", "Lecturas lógicas", "Lecturas lógicas",
        "Tasa HIT", "Tasa HIT", "Tasa HIT", "Tasa HIT","Tasa HIT"
    ]
    })
    fig = px.line(df, x="Segundos", y="Porcentaje", color='Categoría')
    graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", graphJSON = graphJSON)

@app.route('/ping')
def ping():
    return '<p>pong</p>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)