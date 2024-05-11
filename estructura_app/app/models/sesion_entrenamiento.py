from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SesionEntrenamiento(db.Model):
    __tablename__ = 'sesiones_entrenamiento'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    rutina_id = db.Column(db.Integer, db.ForeignKey('rutinas.id'))
    fecha = db.Column(db.Date)
    duracion = db.Column(db.Integer)
    observaciones = db.Column(db.String)

    def __repr__(self):
        return f'<SesionEntrenamiento {self.id}>'
