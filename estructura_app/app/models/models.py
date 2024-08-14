from app import db  # Importa la instancia de la base de datos desde la aplicación principal

# Modelo User que representa la tabla 'users' en la base de datos
class User(db.Model):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)  # Columna 'id' como clave primaria de tipo entero
    username = db.Column(db.String(64), unique=True, nullable=False)  # Columna 'username' de tipo cadena, única y no nula
    email = db.Column(db.String(120), unique=True, nullable=False)  # Columna 'email' de tipo cadena, única y no nula
    password = db.Column(db.String(128), nullable=False)  # Columna 'password' de tipo cadena, no nula
    roles = db.relationship('Role', secondary='users_roles', back_populates='users')  
    # Relación muchos a muchos con el modelo 'Role' usando la tabla de asociación 'users_roles'.
    # Un usuario puede tener múltiples roles y un rol puede pertenecer a múltiples usuarios.

    def __repr__(self):
        # Representación en cadena del objeto User, útil para depuración y logging
        return f"User('{self.username}', '{self.email}')"

# Modelo Role que representa la tabla 'roles' en la base de datos
class Role(db.Model):
    __tablename__ = 'roles'  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)  # Columna 'id' como clave primaria de tipo entero
    name = db.Column(db.String(64), unique=True, nullable=False)  # Columna 'name' de tipo cadena, única y no nula
    users = db.relationship('User', secondary='users_roles', back_populates='roles')  
    # Relación muchos a muchos con el modelo 'User' usando la tabla de asociación 'users_roles'.
    # Un rol puede tener múltiples usuarios y un usuario puede pertenecer a múltiples roles.

    def __repr__(self):
        # Representación en cadena del objeto Role, útil para depuración y logging
        return f"Role('{self.name}')"

# Tabla de asociación 'users_roles' que une la relación muchos a muchos entre usuarios y roles
users_roles = db.Table('users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),  # Columna 'user_id' que referencia la clave primaria de la tabla 'users'
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))  # Columna 'role_id' que referencia la clave primaria de la tabla 'roles'
)
