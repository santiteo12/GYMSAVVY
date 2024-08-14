from flask import Flask, render_template
from flask_migrate import Migrate
from app.config import config
from db import db

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # Configuración de la base de datos
    app.config.from_object(config.Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mauri:123123@localhost:5432/gymsavvy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la instancia de SQLAlchemy con la aplicación Flask
    db.init_app(app)

    # Inicializar Migrate con la aplicación Flask y SQLAlchemy
    migrate = Migrate(app, db)

    # Importar modelos aquí para evitar problemas de importación circular
    with app.app_context():
        from app import models

    # Agregar una ruta raíz para servir como la página principal
    @app.route('/')
    def index():
        return render_template('index.html')

    # Registro de los blueprints
    from app.routes.exercises_routes import exercise_blueprint
    app.register_blueprint(exercise_blueprint)

    from app.routes.models_routes import models_blueprint
    app.register_blueprint(models_blueprint)

    from app.routes.musclegroups_routes import muscle_group_blueprint
    app.register_blueprint(muscle_group_blueprint)
    
    from app.routes.routine_routes import routine_blueprint
    app.register_blueprint(routine_blueprint)
    
    from app.routes.routineexercise_routes import routineexercise_blueprint
    app.register_blueprint(routineexercise_blueprint)

    app.config['SECRET_KEY'] = 'mypassword'

    return app

# Llamar a la función create_app() y asignar el resultado a una variable
app = create_app()

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
