import unittest
from app import create_app, db
from app.models import User, Routine

class TestModels(unittest.TestCase):
    def setUp(self):
        # Configura una aplicación de prueba y una base de datos en memoria
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.appctx = self.app.app_context()
        self.appctx.push()
        # Crea todas las tablas en la base de datos de prueba
        db.create_all()

    def tearDown(self):
        # Elimina la sesión de base de datos y elimina todas las tablas
        db.session.remove()
        db.drop_all()
        self.appctx.pop()

    def test_model_creation(self):
        # Valores predeterminados para los modelos a probar
        default_values = {
            User: {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'password'}
        }
        # Prueba la creación de instancias para los modelos especificados
        for model in [User]:
            instance = model(**default_values[model])
            db.session.add(instance)
            db.session.commit()
            # Verifica que la instancia se haya guardado correctamente en la base de datos
            self.assertEqual(model.query.count(), 1)

    def test_model_relationships(self):
        # Crea un usuario y guárdalo en la base de datos
        user = User(username='testuser', email='testuser@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        # Crea una rutina asociada al usuario y guárdala en la base de datos
        routine = Routine(name='Test Routine', description='This is a test routine', user=user)
        db.session.add(routine)
        db.session.commit()
        # Verifica que tanto el usuario como la rutina se hayan guardado correctamente
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(Routine.query.count(), 1)
        # Verifica que la rutina esté asociada al usuario correcto
        self.assertEqual(routine.user.username, 'testuser')

if __name__ == '__main__':
    unittest.main()
