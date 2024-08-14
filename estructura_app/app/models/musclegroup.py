from app import db  # Importa la instancia de la base de datos desde la aplicación principal

# Modelo MuscleGroup que representa la tabla 'muscle_groups' en la base de datos
class MuscleGroup(db.Model):
    __tablename__ = 'muscle_groups'  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)  # Columna 'id' como clave primaria de tipo entero
    name = db.Column(db.String(64), unique=True, nullable=False)  # Columna 'name' de tipo cadena, única y no nula

    def __repr__(self):
        # Representación en cadena del objeto MuscleGroup, útil para depuración y logging
        return f"MuscleGroup('{self.name}')"
