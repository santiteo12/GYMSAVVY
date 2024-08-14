from flask import Blueprint, request, jsonify, render_template  # Importa los módulos necesarios de Flask
from app import db  # Importa la instancia de la base de datos desde la aplicación principal
from app.models.exercise import Exercise  # Importa el modelo Exercise
from app.models import MuscleGroup  # Importa el modelo MuscleGroup

# Define un Blueprint para agrupar las rutas relacionadas con ejercicios
exercise_blueprint = Blueprint('exercise', __name__, template_folder='../templates')

@exercise_blueprint.route('/')
def exercises():
    # Ruta para obtener todos los ejercicios y renderizar el template 'exercises.html'
    exercises = Exercise.query.all()  # Obtiene todos los ejercicios de la base de datos
    return render_template('exercises.html', exercises=exercises)

@exercise_blueprint.route('/exercises', methods=['GET'])
def get_all_exercises():
    """Obtiene todos los ejercicios y grupos musculares"""
    exercises = Exercise.query.all()  # Obtiene todos los ejercicios de la base de datos
    muscle_groups = MuscleGroup.query.all()  # Obtiene todos los grupos musculares de la base de datos
    return render_template('exercises.html', exercises=exercises, muscle_groups=muscle_groups)

@exercise_blueprint.route('/exercises/<int:exercise_id>', methods=['GET'])
def get_exercise(exercise_id):
    """Obtiene un ejercicio específico por su ID"""
    exercise = Exercise.query.get(exercise_id)  # Busca un ejercicio por su ID
    if exercise is None:
        # Si no se encuentra el ejercicio, devuelve un error 404
        return jsonify({'error': 'Exercise not found'}), 404
    # Si se encuentra, devuelve los datos del ejercicio en formato JSON
    return jsonify(exercise.to_dict())

@exercise_blueprint.route('/exercises', methods=['POST'])
def create_exercise():
    """Crea un nuevo ejercicio"""
    data = request.get_json()  # Obtiene los datos del cuerpo de la solicitud en formato JSON
    if not data or 'name' not in data or 'description' not in data or 'muscle_group_id' not in data:
        # Si faltan datos necesarios, devuelve un error 400
        return jsonify({'error': 'Invalid request'}), 400
    # Crea una nueva instancia de Exercise con los datos proporcionados
    exercise = Exercise(name=data['name'], description=data['description'], muscle_group_id=data['muscle_group_id'])
    db.session.add(exercise)  # Añade el nuevo ejercicio a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    # Devuelve los datos del nuevo ejercicio en formato JSON, con un código 201 de creado
    return jsonify(exercise.to_dict()), 201

@exercise_blueprint.route('/exercises/<int:exercise_id>', methods=['PUT'])
def update_exercise(exercise_id):
    """Actualiza un ejercicio existente"""
    exercise = Exercise.query.get(exercise_id)  # Busca el ejercicio por su ID
    if exercise is None:
        # Si no se encuentra el ejercicio, devuelve un error 404
        return jsonify({'error': 'Exercise not found'}), 404
    data = request.get_json()  # Obtiene los datos del cuerpo de la solicitud en formato JSON
    if not data:
        # Si no se proporcionan datos, devuelve un error 400
        return jsonify({'error': 'Invalid request'}), 400
    # Actualiza los campos del ejercicio con los nuevos datos, o mantiene los existentes si no se proporcionan
    exercise.name = data.get('name', exercise.name)
    exercise.description = data.get('description', exercise.description)
    exercise.muscle_group_id = data.get('muscle_group_id', exercise.muscle_group_id)
    db.session.commit()  # Guarda los cambios en la base de datos
    # Devuelve los datos del ejercicio actualizado en formato JSON
    return jsonify(exercise.to_dict())

@exercise_blueprint.route('/exercises/<int:exercise_id>', methods=['DELETE'])
def delete_exercise(exercise_id):
    """Elimina un ejercicio"""
    exercise = Exercise.query.get(exercise_id)  # Busca el ejercicio por su ID
    if exercise is None:
        # Si no se encuentra el ejercicio, devuelve un error 404
        return jsonify({'error': 'Exercise not found'}), 404
    db.session.delete(exercise)  # Elimina el ejercicio de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    # Devuelve un mensaje de confirmación de la eliminación
    return jsonify({'message': 'Exercise deleted'})

@exercise_blueprint.after_request
def set_response_encoding(response):
    # Establece la codificación de respuesta a UTF-8 para asegurarse de que el contenido se maneje correctamente
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@exercise_blueprint.route('/exercises', methods=['GET', 'POST'])
def manage_exercises():
    if request.method == 'POST':
        # Si el método es POST, crea un nuevo ejercicio
        name = request.json.get('name')
        description = request.json.get('description')
        muscle_group_id = request.json.get('muscle_group_id')
        new_exercise = Exercise(name=name, description=description, muscle_group_id=muscle_group_id)
        db.session.add(new_exercise)  # Añade el nuevo ejercicio a la sesión de la base de datos
        db.session.commit()  # Guarda los cambios en la base de datos
        # Devuelve los datos del nuevo ejercicio en formato JSON
        return jsonify({
            'id': new_exercise.id,
            'name': new_exercise.name,
            'description': new_exercise.description,
            'muscle_group_id': new_exercise.muscle_group_id
        })

    # Si el método es GET, renderiza el template 'exercises.html' con todos los grupos musculares
    muscle_groups = MuscleGroup.query.all()
    return render_template('exercises.html', muscle_groups=muscle_groups)
