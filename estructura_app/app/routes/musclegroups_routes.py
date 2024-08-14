from flask import Blueprint, request, jsonify, render_template, redirect, url_for  # Importa módulos de Flask
from app import db  # Importa la instancia de la base de datos desde la aplicación principal
from app.models.musclegroup import MuscleGroup  # Importa el modelo MuscleGroup

# Define un Blueprint para las rutas relacionadas con los grupos musculares
muscle_group_blueprint = Blueprint('muscle_group', __name__, template_folder='templates')

# Ruta para obtener todos los grupos musculares
@muscle_group_blueprint.route('/muscle_groups', methods=['GET'])
def get_all_muscle_groups():
    muscle_groups = MuscleGroup.query.all()  # Consulta todos los grupos musculares de la base de datos
    return render_template('muscle_groups.html', muscle_groups=muscle_groups)  # Renderiza la plantilla con los grupos musculares

# Ruta para obtener un grupo muscular específico por su ID
@muscle_group_blueprint.route('/muscle_group/<int:muscle_group_id>', methods=['GET'])
def get_muscle_group(muscle_group_id):
    muscle_group = MuscleGroup.query.get(muscle_group_id)  # Busca el grupo muscular por su ID
    if muscle_group is None:
        # Si no se encuentra el grupo muscular, devuelve un error 404
        return jsonify({'error': 'Muscle group not found'}), 404
    # Renderiza la plantilla con el grupo muscular encontrado
    return render_template('muscle_group.html', muscle_group=muscle_group)

# Ruta para crear un nuevo grupo muscular
@muscle_group_blueprint.route('/muscle_group', methods=['POST'])
def create_muscle_group():
    data = request.get_json()  # Obtiene los datos de la solicitud en formato JSON
    if not data or 'name' not in data:
        # Si faltan datos o el nombre, devuelve un error 400
        return jsonify({'error': 'Invalid request'}), 400
    muscle_group = MuscleGroup(name=data['name'])  # Crea una nueva instancia de MuscleGroup con el nombre proporcionado
    db.session.add(muscle_group)  # Añade el nuevo grupo muscular a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    # Redirige a la vista que muestra todos los grupos musculares
    return redirect(url_for('muscle_group.get_all_muscle_groups')), 201

# Ruta para actualizar un grupo muscular existente
@muscle_group_blueprint.route('/muscle_group/<int:muscle_group_id>', methods=['PUT'])
def update_muscle_group(muscle_group_id):
    muscle_group = MuscleGroup.query.get(muscle_group_id)  # Busca el grupo muscular por su ID
    if muscle_group is None:
        # Si no se encuentra el grupo muscular, devuelve un error 404
        return jsonify({'error': 'Muscle group not found'}), 404
    data = request.get_json()  # Obtiene los datos de la solicitud en formato JSON
    if not data:
        # Si no se proporcionan datos, devuelve un error 400
        return jsonify({'error': 'Invalid request'}), 400
    muscle_group.name = data.get('name', muscle_group.name)  # Actualiza el nombre del grupo muscular, si se proporciona
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify(muscle_group.to_dict())  # Devuelve los datos del grupo muscular actualizado en formato JSON

# Ruta para eliminar un grupo muscular existente
@muscle_group_blueprint.route('/muscle_group/<int:muscle_group_id>', methods=['DELETE'])
def delete_muscle_group(muscle_group_id):
    muscle_group = MuscleGroup.query.get(muscle_group_id)  # Busca el grupo muscular por su ID
    if muscle_group is None:
        # Si no se encuentra el grupo muscular, devuelve un error 404
        return jsonify({'error': 'Muscle group not found'}), 404
    db.session.delete(muscle_group)  # Elimina el grupo muscular de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify({'message': 'Muscle group deleted'})  # Devuelve un mensaje confirmando la eliminación
