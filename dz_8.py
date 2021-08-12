from sqlalchemy import create_engine, Table, Column, Integer, String
from sqlalchemy.sql.schema import MetaData
from sqlalchemy import select
from sqlalchemy import and_, or_

engine = create_engine('sqlite:///college.db')
connection = engine.connect()
meta = MetaData()

departments = Table(
    'departmments', meta,
    Column('id', Integer, primary_key=True),
    Column('department_name', String),
)

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('department_id', Integer)
)

training_courses = Table(
    'training_courses', meta,
    Column('id', Integer, primary_key=True),
    Column('trining_course_name', String),
    Column('department_id', Integer)
)
meta.create_all(engine)

# connection.execute(
#     departments.
#     insert(),
#     [
#         {'id': '1', 'department_name': 'ФПМИ'},
#         {'id': '2', 'department_name': 'Химический'},
#         {'id': '3', 'department_name': 'Биологический'}
#     ]
# )

# connection.execute(
#     students.
#     insert(),
#     [
#         {'id': '1', 'first_name': 'Grisha', 'last_name': 'Perelman', 'department_id': '1'},
#         {'id': '2', 'first_name': 'Ada', 'last_name': 'Lovelace', 'department_id': '1'},
#         {'id': '3', 'first_name': 'Blaise', 'last_name': 'Pascal', 'department_id': '1'},
#         {'id': '4', 'first_name': 'Amedeo', 'last_name': 'Avogadro', 'department_id': '2'},
#         {'id': '5', 'first_name': 'Dmitriy', 'last_name': 'Mendeleev', 'department_id': '2'},
#         {'id': '6', 'first_name': 'Marie', 'last_name': 'Curie', 'department_id': '2'},
#         {'id': '7', 'first_name': 'Charles', 'last_name': 'Darwin', 'department_id': '3'},
#         {'id': '8', 'first_name': 'Gregor', 'last_name': 'Mendel', 'department_id': '3'},
#         {'id': '9', 'first_name': 'Rosa', 'last_name': 'Franklin', 'department_id': '3'}
#     ]
# )

# connection.execute(
#     training_courses.
#     insert(),
#     [
#         {'id': '1', 'trining_course_name': 'Введение в высшую математику', 'department_id': '1'},
#         {'id': '2', 'trining_course_name': 'Основы математического анализа', 'department_id': '1'},
#         {'id': '3', 'trining_course_name': 'Теория информации', 'department_id': '1'},
#         {'id': '4', 'trining_course_name': 'Общая химия', 'department_id': '2'},
#         {'id': '5', 'trining_course_name': 'Органическая химия', 'department_id': '2'},
#         {'id': '6', 'trining_course_name': 'Аналитическая химия', 'department_id': '2'},
#         {'id': '7', 'trining_course_name': 'Общая биология', 'department_id': '3'},
#         {'id': '8', 'trining_course_name': 'Биохимия', 'department_id': '3'},
#         {'id': '9', 'trining_course_name': 'Молекулярная биология', 'department_id': '3'}

        
#     ]
# )

# j = departments.join(training_courses, departments.c.id == training_courses.c.department_id)

# stmt = select([departments, training_courses]).select_from(j)

# result = connection.execute(stmt).fetchall()

# print(result)


j = students.join(departments, students.c.department_id == departments.c.id)

stmt = select([students, departments]).select_from(j)

result = connection.execute(stmt).fetchall()

print(result)