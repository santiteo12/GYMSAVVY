from . import db  # Importar la instancia de la base de datos de SQLAlchemy

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo_electronico = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer)
    género = db.Column(db.String(10))
    altura = db.Column(db.Float)
    peso = db.Column(db.Float)
    objetivo = db.Column(db.String(50))
    
    # Relaciones
    rutinas = db.relationship('Rutina', backref='usuario', lazy=True)
    sesiones = db.relationship('SesionEntrenamiento', backref='usuario', lazy=True)
    progresos = db.relationship('Progreso', backref='usuario', lazy=True)

# Se pueden agregar otros modelos relacionados aquí o en otros archivos

