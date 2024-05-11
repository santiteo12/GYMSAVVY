from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Progreso(db.Model):
    __tablename__ = 'progresos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    ejercicio_id = db.Column(db.Integer, db.ForeignKey('ejercicios.id'))
    fecha = db.Column(db.Date)
    peso_levantado = db.Column(db.Float)
    repeticiones = db.Column(db.Integer)
    series = db.Column(db.Integer)
    notas = db.Column(db.String)

    def __repr__(self):
        return f'<Progreso {self.id}>'
