from app import db  # Importa la instancia de la base de datos desde la aplicación principal

# Define la tabla de asociación 'routine_exercises' que une la relación muchos a muchos entre rutinas y ejercicios
routine_exercises = db.Table('routine_exercises',
    db.Column('routine_id', db.Integer, db.ForeignKey('routines.id'), primary_key=True),  
    # Columna 'routine_id' que referencia la clave primaria de la tabla 'routines'. También es clave primaria en esta tabla.
    
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id'), primary_key=True)  
    # Columna 'exercise_id' que referencia la clave primaria de la tabla 'exercises'. También es clave primaria en esta tabla.
)