def test_musclegroup_model(new_app, db_session):
    # Importa el modelo MuscleGroup desde la aplicación
    from app.models.musclegroup import MuscleGroup

    # Crea una instancia del modelo MuscleGroup con el nombre 'Back'
    muscle_group = MuscleGroup(name='Back')

    # Agrega la instancia a la sesión de base de datos y confirma los cambios
    db_session.add(muscle_group)
    db_session.commit()

    # Verifica que el grupo muscular se haya agregado correctamente a la sesión de base de datos
    assert muscle_group in db_session
    # Verifica que el nombre del grupo muscular sea el esperado
    assert muscle_group.name == 'Back'

    # Elimina el grupo muscular de la base de datos y confirma los cambios
    db_session.delete(muscle_group)
    db_session.commit()
    # Cierra la sesión de base de datos
    db_session.close()
