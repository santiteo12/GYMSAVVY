from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ejercicio(db.Model):
    __tablename__ = 'ejercicios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    descripcion = db.Column(db.String)
    grupo_muscular = db.Column(db.String)

    def __repr__(self):
        return f'<Ejercicio {self.id}>'
