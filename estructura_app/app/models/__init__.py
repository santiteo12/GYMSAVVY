from flask_sqlalchemy import SQLAlchemy

# Inicializa la instancia de la base de datos
db = SQLAlchemy()

# Importa todos los modelos aquí para asegurar que se registren adecuadamente en el objeto db
from .usuario import Usuario
from .role import Role  # Asumiendo que tienes un modelo Role definido
from .ejercicio import Ejercicio
from .rutina import Rutina, RutinaEjercicio

# Esto permite hacer desde otros lugares: from app.models import Usuario, Ejercicio, etc.

