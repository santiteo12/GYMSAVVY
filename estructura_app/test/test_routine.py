def test_routine_model(db_session, create_user, create_routine, create_tables):
    # Obtiene el usuario y la rutina creados por las fixtures
    user = create_user  # No necesitas llamar a create_user con paréntesis
    routine = create_routine  # No necesitas llamar a create_routine con paréntesis

    # No es necesario agregar el usuario y la rutina a la sesión de base de datos porque ya se agregaron en las fixtures
    # db_session.add(user)
    # db_session.add(routine)
    # db_session.commit()

    # Verifica que la rutina se haya agregado correctamente a la sesión de base de datos
    assert routine in db_session
    # Verifica que la rutina esté asociada al usuario correcto
    assert routine.user.username == 'testuser'
