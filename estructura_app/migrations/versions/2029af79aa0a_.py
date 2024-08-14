from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2029af79aa0a'
down_revision = None
branch_labels = None
depends_on = None

# Definir la tabla muscle_groups
muscle_groups_table = sa.Table(
    'muscle_groups',
    sa.MetaData(),
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String(128), nullable=False)
)

def upgrade():
    # Crea las tablas en la base de datos
    op.create_table('muscle_groups',
        sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('muscle_groups_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='muscle_groups_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_table('roles',
        sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('roles_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='roles_pkey'),
        sa.UniqueConstraint('name', name='roles_name_key'),
        postgresql_ignore_search_path=False
    )
    op.create_table('users',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
        sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
        sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='users_pkey'),
        sa.UniqueConstraint('email', name='users_email_key'),
        sa.UniqueConstraint('username', name='users_username_key')
    )
    op.create_table('exercises',
        sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('exercises_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
        sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column('muscle_group_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['muscle_group_id'], ['muscle_groups.id'], name='fk_muscle_group'),
        sa.PrimaryKeyConstraint('id', name='exercises_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_table('routines',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
        sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='routines_user_id_fkey'),
        sa.PrimaryKeyConstraint('id', name='routines_pkey')
    )
    op.create_table('users_roles',
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name='users_roles_role_id_fkey'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='users_roles_user_id_fkey')
    )
    op.create_table('routine_exercises',
        sa.Column('routine_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('exercise_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], name='routine_exercises_exercise_id_fkey'),
        sa.ForeignKeyConstraint(['routine_id'], ['routines.id'], name='routine_exercises_routine_id_fkey'),
        sa.PrimaryKeyConstraint('routine_id', 'exercise_id', name='routine_exercises_pkey')
    )

    # Insertar datos en la tabla muscle_groups
    op.bulk_insert(muscle_groups_table, [
        {'id': 1, 'name': 'Pecho'},
        {'id': 2, 'name': 'Espalda'},
        {'id': 3, 'name': 'Piernas'},
        {'id': 4, 'name': 'Brazos'}
    ])

def downgrade():
    # Elimina las tablas de asociación y las tablas que dependen de otras.
    op.drop_table('routine_exercises')
    op.drop_table('users_roles')
    
    # Luego elimina las tablas dependientes.
    op.drop_table('exercises')
    op.drop_table('routines')
    op.drop_table('roles')
    op.drop_table('muscle_groups')
    op.drop_table('users')
