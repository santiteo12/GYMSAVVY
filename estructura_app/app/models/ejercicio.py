from . import db

class Ejercicio(db.Model):
    __tablename__ = 'ejercicios'

    id_ejercicio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    grupo_muscular = db.Column(db.String(50))

    # Relaciones
    rutinas = db.relationship('RutinaEjercicio', back_populates='ejercicio')
