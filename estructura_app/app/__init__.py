from flask import Flask
from flask_marshmallow import Marshmallow
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from db import init_db, db  # Importa la función init_db y la instancia db


migrate = Migrate()
ma = Marshmallow()

def create_app() -> Flask:  # Retorna una instancia de Flask
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')

    # https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # No es necesario asignar db a app.db, ya que db es una instancia global

    # https://flask.palletsprojects.com/es/main/blueprints/
    from app.resources import home
    app.register_blueprint(home, url_prefix='/api/v1')

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}  # Agrega db al contexto de shell

    return app
