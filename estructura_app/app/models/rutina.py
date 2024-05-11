from . import db

class Rutina(db.Model):
    __tablename__ = 'rutinas'

    id_rutina = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    duracion_estimada = db.Column(db.Integer)

    # Relaciones
    ejercicios = db.relationship('RutinaEjercicio', back_populates='rutina')

class RutinaEjercicio(db.Model):
    __tablename__ = 'rutina_ejercicio'
    id_rutina = db.Column(db.Integer, db.ForeignKey('rutinas.id_rutina'), primary_key=True)
    id_ejercicio = db.Column(db.Integer, db.ForeignKey('ejercicios.id_ejercicio'), primary_key=True)
    ejercicio = db.relationship('Ejercicio', back_populates='rutinas')
    rutina = db.relationship('Rutina', back_populates='ejercicios')
