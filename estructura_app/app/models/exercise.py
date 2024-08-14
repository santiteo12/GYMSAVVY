from app import db
from app.models.routineexercise import routine_exercises  # Importa la tabla de asociación desde routineexercise.py

class Exercise(db.Model):
    __tablename__ = 'exercises'  # Define el nombre de la tabla en la base de datos

    # Definición de las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # Columna 'id' como clave primaria y de tipo entero
    name = db.Column(db.String(128), nullable=False)  # Columna 'name' de tipo cadena con un máximo de 128 caracteres, no puede ser nula
    description = db.Column(db.Text, nullable=False)  # Columna 'description' de tipo texto, no puede ser nula
    muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_groups.id'), nullable=False)  # Columna 'muscle_group_id' con una clave foránea que referencia la tabla 'muscle_groups', no puede ser nula

    # Relaciones
    muscle_group = db.relationship('MuscleGroup', backref=db.backref('exercises', lazy=True))  
    # Define una relación con el modelo 'MuscleGroup'. Un ejercicio pertenece a un grupo muscular.
    # El parámetro 'backref' crea un acceso inverso, permitiendo que un grupo muscular acceda a todos los ejercicios asociados.
    
    exercise_routines = db.relationship('Routine', secondary=routine_exercises, back_populates='exercises')  
    # Define una relación secundaria con el modelo 'Routine' a través de la tabla de asociación 'routine_exercises'.
    # Un ejercicio puede estar asociado a múltiples rutinas.

    def __init__(self, name, description, muscle_group_id=None):
        # Constructor de la clase, inicializa las propiedades del objeto Exercise
        self.name = name
        self.description = description
        self.muscle_group_id = muscle_group_id

    def to_dict(self):
        # Método para convertir un objeto Exercise en un diccionario, útil para serialización
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'muscle_group_id': self.muscle_group_id
        }
