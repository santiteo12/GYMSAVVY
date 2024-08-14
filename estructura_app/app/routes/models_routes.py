from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Role, users_roles  # Importamos los modelos User, Role y la tabla users_roles

# Creamos un blueprint para las rutas de usuarios y roles
models_blueprint = Blueprint('users_roles', __name__)

# Ruta para obtener todos los usuarios
@models_blueprint.route('/users', methods=['GET'])
def get_users():
    # Obtenemos todos los usuarios de la base de datos
    users = User.query.all()
    # Convertimos los usuarios a una lista de diccionarios
    users_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'roles': [role.name for role in user.roles]} for user in users]
    # Devolvemos la lista de usuarios en formato JSON
    return jsonify(users_list)

# Ruta para obtener un usuario por ID
@models_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Obtenemos el usuario con el ID especificado
    user = User.query.get(user_id)
    # Si el usuario no existe, devolvemos un error 404
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    # Convertimos el usuario a un diccionario
    user_dict = {'id': user.id, 'username': user.username, 'email': user.email, 'roles': [role.name for role in user.roles]}
    # Devolvemos el usuario en formato JSON
    return jsonify(user_dict)

# Ruta para crear un nuevo usuario
@models_blueprint.route('/users', methods=['POST'])
def create_user():
    # Obtenemos los datos del usuario desde la solicitud
    data = request.get_json()
    # Creamos un nuevo usuario con los datos proporcionados
    user = User(username=data['username'], email=data['email'], password=data['password'])
    # Agregamos el usuario a la base de datos
    db.session.add(user)
    db.session.commit()
    # Devolvemos el usuario creado en formato JSON
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201

# Ruta para asignar un role a un usuario
@models_blueprint.route('/users/<int:user_id>/roles/<int:role_id>', methods=['POST'])
def assign_role(user_id, role_id):
    # Obtenemos el usuario y el role con los IDs especificados
    user = User.query.get(user_id)
    role = Role.query.get(role_id)
    # Si el usuario o el role no existen, devolvemos un error 404
    if user is None or role is None:
        return jsonify({'error': 'User or role not found'}), 404
    # Asignamos el role al usuario
    user.roles.append(role)
    db.session.commit()
    # Devolvemos un mensaje de éxito
    return jsonify({'message': 'Role assigned successfully'})

# Ruta para obtener todos los roles
@models_blueprint.route('/roles', methods=['GET'])
def get_roles():
    # Obtenemos todos los roles de la base de datos
    roles = Role.query.all()
    # Convertimos los roles a una lista de diccionarios
    roles_list = [{'id': role.id, 'name': role.name, 'users': [user.username for user in role.users]} for role in roles]
    # Devolvemos la lista de roles en formato JSON
    return jsonify(roles_list)

# Ruta para obtener un role por ID
@models_blueprint.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    # Obtenemos el role con el ID especificado
    role = Role.query.get(role_id)
    # Si el role no existe, devolvemos un error 404
    if role is None:
        return jsonify({'error': 'Role not found'}), 404
    # Convertimos el role a un diccionario
    role_dict = {'id': role.id, 'name': role.name, 'users': [user.username for user in role.users]}
    # Devolvemos el role en formato JSON
    return jsonify(role_dict)