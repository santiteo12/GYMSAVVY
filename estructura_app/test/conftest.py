# tests/conftest.py

import pytest
from app import create_app
from app.models import User, MuscleGroup, Role, Exercise, Routine
from db import db

# Configura una aplicación de Flask para pruebas con una base de datos temporal
@pytest.fixture(scope='session')
def new_app():
    app = create_app()
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'postgresql://faustillo:comoera01@localhost:5432/gymsavvy',
        'TESTING': True,
    })
    yield app
    # Después de las pruebas, se eliminan todas las tablas de la base de datos
    with app.app_context():
        db.drop_all()

# Crea todas las tablas en la base de datos antes de cada prueba
@pytest.fixture(scope='function', autouse=True)
def create_tables(new_app):
    with new_app.app_context():
        db.create_all()

# Proporciona un cliente de prueba para realizar solicitudes HTTP a la aplicación
@pytest.fixture(scope='function')
def client(new_app):
    return new_app.test_client()

# Proporciona una sesión de base de datos para cada prueba y revierte los cambios al final
@pytest.fixture(scope='function')
def db_session(new_app):
    with new_app.app_context():
        yield db.session
        db.session.rollback()

# Función de utilidad para crear un usuario
def create_user(username='testuser', email='testuser@example.com', password='password'):
    return User(username=username, email=email, password=password)

# Fixture para crear un grupo muscular y guardarlo en la base de datos
@pytest.fixture
def create_musclegroup(db_session):
    muscle_group = MuscleGroup(name='Chest')
    db_session.add(muscle_group)
    db_session.commit()
    return muscle_group

# Función de utilidad para crear un rol
def create_role(name='Admin'):
    return Role(name=name)

# Fixture para crear un ejercicio asociado a un grupo muscular
@pytest.fixture(scope='function')
def create_exercise(create_musclegroup, db_session):
    exercise = Exercise(name='Bench Press', description='A chest exercise', muscle_group=create_musclegroup)
    db_session.add(exercise)
    db_session.commit()
    return exercise

# Fixture para crear un usuario y guardarlo en la base de datos
@pytest.fixture(scope='function')
def create_user(db_session):
    user = User(username='testuser', email='testuser@example.com', password='password')
    db_session.add(user)
    db_session.commit()
    return user

# Fixture para crear una rutina y guardarla en la base de datos
@pytest.fixture(scope='function')
def create_routine(create_user, db_session):
    routine = Routine(name='My Routine', description='This is a test routine', user=create_user)
    db_session.add(routine)
    db_session.commit()
    return routine

# Función para configurar la base de datos de pruebas
def setup_test_db():
    db.create_all()

# Función para limpiar la base de datos de pruebas
def teardown_test_db():
    db.session.remove()
    db.drop_all()
