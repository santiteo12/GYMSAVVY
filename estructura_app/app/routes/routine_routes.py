from flask import Blueprint, request, jsonify, render_template  # Importa los módulos necesarios de Flask
from app.models import Routine, Exercise  # Importa los modelos Routine y Exercise
from app import db  # Importa la instancia de la base de datos

# Define un Blueprint para manejar las rutas relacionadas con las rutinas
routine_blueprint = Blueprint('routine', __name__)

# Ruta para crear una nueva rutina
@routine_blueprint.route('/routines', methods=['POST'])
def create_routine():
    data = request.get_json()  # Obtiene los datos de la solicitud en formato JSON
    routine = Routine(name=data['name'], description=data['description'])  # Crea una nueva instancia de Routine
    db.session.add(routine)  # Añade la rutina a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify(routine.to_dict()), 201  # Devuelve la rutina creada en formato JSON

# Ruta para obtener todas las rutinas
@routine_blueprint.route('/routines', methods=['GET'])
def get_routines():
    routines = Routine.query.all()  # Consulta todas las rutinas en la base de datos
    exercises = Exercise.query.all()  # Obtiene todos los ejercicios
    return render_template('routines.html', routines=routines, exercises=exercises)  # Renderiza la plantilla con rutinas y ejercicios

# Ruta para obtener una rutina específica por su ID
@routine_blueprint.route('/routines/<int:routine_id>', methods=['GET'])
def get_routine(routine_id):
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine is None:
        return jsonify({'error': 'Routine not found'}), 404  # Devuelve un error si la rutina no se encuentra
    return render_template('routine_detail.html', routine=routine)  # Renderiza la plantilla con los detalles de la rutina

# Ruta para actualizar una rutina existente
@routine_blueprint.route('/routines/<int:routine_id>', methods=['PUT'])
def update_routine(routine_id):
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine is None:
        return jsonify({'error': 'Routine not found'}), 404  # Devuelve un error si la rutina no se encuentra
    data = request.get_json()  # Obtiene los datos de la solicitud en formato JSON
    routine.name = data['name']  # Actualiza el nombre de la rutina
    routine.description = data['description']  # Actualiza la descripción de la rutina
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify(routine.to_dict())  # Devuelve la rutina actualizada en formato JSON

# Ruta para eliminar una rutina existente
@routine_blueprint.route('/routines/<int:routine_id>', methods=['DELETE'])
def delete_routine(routine_id):
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine is None:
        return jsonify({'error': 'Routine not found'}), 404  # Devuelve un error si la rutina no se encuentra
    db.session.delete(routine)  # Elimina la rutina de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify({'message': 'Routine deleted'})  # Devuelve un mensaje de confirmación

# Ruta para agregar un ejercicio a una rutina
@routine_blueprint.route('/routines/<int:routine_id>/exercises', methods=['POST'])
def add_exercise_to_routine(routine_id):
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine is None:
        return jsonify({'error': 'Routine not found'}), 404  # Devuelve un error si la rutina no se encuentra
    data = request.get_json()  # Obtiene los datos de la solicitud en formato JSON
    exercise_id = data['exercise_id']  # Obtiene el ID del ejercicio a agregar
    exercise = Exercise.query.get(exercise_id)  # Busca el ejercicio por su ID
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404  # Devuelve un error si el ejercicio no se encuentra
    routine.exercises.append(exercise)  # Agrega el ejercicio a la rutina
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify(routine.to_dict())  # Devuelve la rutina actualizada en formato JSON

# Ruta para obtener los ejercicios asociados a una rutina específica
@routine_blueprint.route('/routines/<int:routine_id>/exercises', methods=['GET'])
def get_exercises_for_routine(routine_id):
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine is None:
        return jsonify({'error': 'Routine not found'}), 404  # Devuelve un error si la rutina no se encuentra
    exercises = routine.exercises  # Obtiene los ejercicios asociados a la rutina
    return jsonify([exercise.to_dict() for exercise in exercises])  # Devuelve la lista de ejercicios en formato JSON

# Ruta para obtener todos los ejercicios
@routine_blueprint.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()  # Obtiene todos los ejercicios en la base de datos
    return jsonify([exercise.to_dict() for exercise in exercises])  # Devuelve la lista de ejercicios en formato JSON

# Ruta para ver una rutina específica (basada en el requerimiento del usuario)
@routine_blueprint.route('/view_routine', methods=['GET'])
def view_routine():
    routines = Routine.query.all()  # Obtiene todas las rutinas
    return render_template('view_routine.html', routines=routines)  # Renderiza la plantilla para ver las rutinas

# Ruta para obtener los datos de una rutina específica
@routine_blueprint.route('/get_routine_data', methods=['GET'])
def get_routine_data():
    routine_id = request.args.get('routine_id')  # Obtiene el ID de la rutina de los parámetros de la URL
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine:
        return jsonify({
            'name': routine.name,
            'description': routine.description,
            'exercises': [{'name': exercise.name} for exercise in routine.exercises]  # Devuelve los nombres de los ejercicios
        })
    else:
        return jsonify({'error': 'Rutina no encontrada'})  # Devuelve un error si la rutina no se encuentra
