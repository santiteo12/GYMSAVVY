from flask import Blueprint, request, jsonify, render_template  # Importa los módulos necesarios de Flask
from app import db  # Importa la instancia de la base de datos
from app.models import Exercise, Routine, routine_exercises  # Importa el modelo Exercise, Routine, y la tabla de asociación routine_exercises

# Define un Blueprint para manejar las rutas relacionadas con ejercicios dentro de rutinas
routineexercise_blueprint = Blueprint('exercises', __name__, template_folder='../templates')

# Ruta para eliminar un ejercicio de la base de datos
@routineexercise_blueprint.route('/exercises/<int:exercise_id>', methods=['DELETE'])
def delete_exercise(exercise_id):
    exercise = Exercise.query.get(exercise_id)  # Busca el ejercicio por su ID
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404  # Devuelve un error si el ejercicio no se encuentra
    db.session.delete(exercise)  # Elimina el ejercicio de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify({'message': 'Exercise deleted successfully'})  # Devuelve un mensaje de confirmación

# Ruta para agregar un ejercicio a una rutina
@routineexercise_blueprint.route('/routines/<int:routine_id>/exercises/<int:exercise_id>', methods=['POST'])
def add_exercise_to_routine(routine_id, exercise_id):
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine is None:
        return jsonify({'error': 'Routine not found'}), 404  # Devuelve un error si la rutina no se encuentra
    exercise = Exercise.query.get(exercise_id)  # Busca el ejercicio por su ID
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404  # Devuelve un error si el ejercicio no se encuentra
    routine.exercises.append(exercise)  # Agrega el ejercicio a la lista de ejercicios de la rutina
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify({'message': 'Exercise added to routine successfully'})  # Devuelve un mensaje de confirmación

# Ruta para eliminar un ejercicio de una rutina
@routineexercise_blueprint.route('/routines/<int:routine_id>/exercises/<int:exercise_id>', methods=['DELETE'])
def remove_exercise_from_routine(routine_id, exercise_id):
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine is None:
        return jsonify({'error': 'Routine not found'}), 404  # Devuelve un error si la rutina no se encuentra
    exercise = Exercise.query.get(exercise_id)  # Busca el ejercicio por su ID
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404  # Devuelve un error si el ejercicio no se encuentra
    routine.exercises.remove(exercise)  # Elimina el ejercicio de la lista de ejercicios de la rutina
    db.session.commit()  # Guarda los cambios en la base de datos
    return jsonify({'message': 'Exercise removed from routine successfully'})  # Devuelve un mensaje de confirmación

# Ruta para obtener los datos de una rutina específica, incluidos los ejercicios
@routineexercise_blueprint.route('/get_routine_data', methods=['GET'])
def get_routine_data():
    routine_id = request.args.get('routine_id')  # Obtiene el ID de la rutina de los parámetros de la URL
    routine = Routine.query.get(routine_id)  # Busca la rutina por su ID
    if routine is None:
        return jsonify({'error': 'Routine not found'}), 404  # Devuelve un error si la rutina no se encuentra

    exercises = routine.exercises.all()  # Obtiene todos los ejercicios asociados a la rutina
    exercise_data = [{'id': exercise.id, 'name': exercise.name} for exercise in exercises]  # Crea una lista de diccionarios con los datos de los ejercicios

    routine_data = {
        'id': routine.id,
        'name': routine.name,
        'description': routine.description,
        'exercises': exercise_data  # Añade la lista de ejercicios a los datos de la rutina
    }

    return jsonify(routine_data)  # Devuelve los datos de la rutina en formato JSON
