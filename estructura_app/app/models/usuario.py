from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    correo = db.Column(db.String, unique=True)
    contraseña = db.Column(db.String)
    edad = db.Column(db.Integer)
    genero = db.Column(db.String)
    altura = db.Column(db.Float)
    peso = db.Column(db.Float)
    objetivo = db.Column(db.String)

    def __repr__(self):
        return f'<Usuario {self.id}>'
