import pytest
from app import db
from app.models.exercise import Exercise
from .conftest import create_musclegroup

def test_exercise_model(db_session, create_musclegroup):
        muscle_group = create_musclegroup
        db_session.add(muscle_group)
        db_session.commit()

        # Actualizar el objeto muscle_group con los datos de la base de datos
        db_session.refresh(muscle_group)

        exercise = Exercise(name='Bench Press', description='A chest exercise', muscle_group_id=muscle_group.id)

        db_session.add(exercise)
        db_session.commit()

        assert exercise in db_session
        assert exercise.name == 'Bench Press'
        assert exercise.description == 'A chest exercise'
        assert exercise.muscle_group == muscle_group