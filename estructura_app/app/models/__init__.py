from flask_sqlalchemy import SQLAlchemy

# Inicializa la instancia de la base de datos
db = SQLAlchemy()

# Importa todos los modelos aquí para asegurar que se registren adecuadamente en el objeto db
from .usuario import Usuario
from .ejercicio import Ejercicio
from .rutina import Rutina
from .sesion_entrenamiento import SesionEntrenamiento
from .progreso import Progreso

# Esto permite hacer desde otros lugares: from app.models import Usuario, Ejercicio, etc.
