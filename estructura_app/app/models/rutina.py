from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rutina(db.Model):
    __tablename__ = 'rutinas'

    id = db.Column(db.Integer, primary_key=True)
    ejercicio_id = db.Column(db.Integer, db.ForeignKey('ejercicios.id'))
    nombre = db.Column(db.String)
    descripcion = db.Column(db.String)
    duracion = db.Column(db.Integer)

    def __repr__(self):
        return f'<Rutina {self.id}>'
