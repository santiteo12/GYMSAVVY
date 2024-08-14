from app import db
from app.models.routineexercise import routine_exercises  # Importa la tabla de asociación desde routineexercise.py
from app.models.exercise import Exercise  # Importa el modelo Exercise

# Modelo Routine que representa la tabla 'routines' en la base de datos
class Routine(db.Model):
    __tablename__ = 'routines'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Columna 'id' como clave primaria de tipo entero
    name = db.Column(db.String(128), nullable=False)  # Columna 'name' de tipo cadena, no nula, con un máximo de 128 caracteres
    description = db.Column(db.Text, nullable=False)  # Columna 'description' de tipo texto, no nula

    exercises = db.relationship('Exercise', secondary=routine_exercises, back_populates='exercise_routines')  
    # Relación muchos a muchos con el modelo 'Exercise' usando la tabla de asociación 'routine_exercises'.
    # Una rutina puede contener múltiples ejercicios, y un ejercicio puede pertenecer a múltiples rutinas.

    def __init__(self, name, description):
        # Constructor de la clase, inicializa las propiedades del objeto Routine
        self.name = name
        self.description = description

    def to_dict(self):
        # Método para convertir un objeto Routine en un diccionario, útil para serialización
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'exercises': [exercise.to_dict() for exercise in self.exercises]  # Convierte cada ejercicio asociado en un diccionario
        }
