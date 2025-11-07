"""Conexión con la base de datos SQL Server usando Flask y SQLAlchemy"""
import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

def strtobool(val):
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    else:
        raise ValueError(f"Invalid truth value {val!r}")


load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Configuración base
app.config["SQL_USER"] = os.getenv("SQL_USER")
app.config["SQL_PASSWORD"] = os.getenv("SQL_PASSWORD")
app.config["SQL_HOST"] = os.getenv("SQL_HOST")
app.config["SQL_DB"] = os.getenv("SQL_DB")
app.config["SQL_WINDOWS_AUTH"] = bool(strtobool(os.getenv("SQL_WINDOWS_AUTH", "False")))

# Construcción de la cadena de conexión
if app.config["SQL_WINDOWS_AUTH"]:
    connection_str = (
        f"mssql+pyodbc://@{app.config['SQL_HOST']}/{app.config['SQL_DB']}?"
        "driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
else:
    connection_str = (
        f"mssql+pyodbc://{app.config['SQL_USER']}:{app.config['SQL_PASSWORD']}@"
        f"{app.config['SQL_HOST']}/{app.config['SQL_DB']}?"
        "driver=ODBC+Driver+17+for+SQL+Server"
    )

# Configuración final
app.config["SQLALCHEMY_DATABASE_URI"] = connection_str
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicialización
db_alchemy = SQLAlchemy(app)
migrate = Migrate(app, db_alchemy)

__all__ = ["app", "db_alchemy"]
