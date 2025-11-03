"""
Aplicación flask para Big Data (conceptos)
"""
from flask import render_template
from python.db_connection import app
import os

app.config["DEBUG"] = True
# pip install -r requirements.txt
# Usar en terminal: flask --app app run --debug


@app.route("/")
def index():
    """retornamos la pagina web"""
    print("Directorio actual:", os.getcwd())
    print("Contenido de templates:", os.listdir("templates"))
    return render_template("index.html")


@app.route("/reports")
def reports():
    """
    Página para mostrar mapa mental sobre Regresión logistica
    """
    return render_template("html/dw/reports.html")

if __name__ == "__main__":
    app.run(debug=True)
