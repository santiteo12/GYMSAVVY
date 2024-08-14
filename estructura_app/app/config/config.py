from dotenv import load_dotenv  # Importa la función para cargar variables de entorno desde un archivo .env
from pathlib import Path  # Importa Path para manejar rutas de archivos
import os  # Importa el módulo os para interactuar con el sistema operativo

# Define el directorio base del proyecto (dos niveles por encima del archivo actual)
basedir = os.path.abspath(Path(__file__).parents[2])

# Carga las variables de entorno desde el archivo .env ubicado en el directorio base
load_dotenv(os.path.join(basedir, '.env'))

# Clase base de configuración que establece los parámetros comunes
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')  # URI de la base de datos desde la variable de entorno
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones de objetos para ahorrar memoria
    SQLALCHEMY_ECHO = False  # Desactiva el registro de todas las consultas SQL en la consola
    TESTING = True  # Activa el modo de prueba

    @staticmethod
    def init_app(app):
        # Método para inicializar la configuración en la aplicación Flask, se puede sobrescribir en subclases
        pass

# Clase de configuración para el entorno de desarrollo
class DevelopmentConfig(Config):
    TESTING = True  # Activa el modo de prueba
    DEBUG = True  # Activa el modo de depuración
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # Activa el seguimiento de modificaciones de objetos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI', 'postgresql://mauri:123123@localhost:5432/gymsavvy')  
    # URI de la base de datos para desarrollo, obtenida de la variable de entorno o una URI por defecto

# Clase de configuración para el entorno de producción
class ProductionConfig(Config):
    DEBUG = False  # Desactiva el modo de depuración
    TESTING = False  # Desactiva el modo de prueba
    SQLALCHEMY_RECORD_QUERIES = False  # Desactiva el registro de consultas SQL para mejorar el rendimiento
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')  # URI de la base de datos para producción

    @classmethod
    def init_app(cls, app):
        # Inicializa la configuración en la aplicación Flask, llamando al método de la clase base
        Config.init_app(app)

# Función de fábrica para obtener la configuración según el entorno
def factory(config_name):
    configuration = {
        'development': DevelopmentConfig,  # Configuración para desarrollo
        'production': ProductionConfig  # Configuración para producción
    }
    
    # Retorna la configuración correspondiente al nombre proporcionado o la de desarrollo por defecto
    return configuration.get(config_name, DevelopmentConfig)
