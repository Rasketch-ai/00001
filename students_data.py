import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import literal_column
from sqlalchemy.orm import aliased
from sqlalchemy.orm import Query
import sys
from IPython.display import HTML, display
from sqlalchemy import func

DeclBase = declarative_base()
engine = sqlalchemy.create_engine('sqlite:///test.db', echo=False)  # echo=True для логгинга
Session = sessionmaker(bind=engine)
session = Session()

class Student(DeclBase):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    program_id = Column(Integer, ForeignKey('programs.id'))
    card = Column(String)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)

    courses = relationship("Course", secondary='marks', back_populates="students")
    programs = relationship("Program", backref='students')

    def __init__(self, card, surname, name, patr, pr):
        self.card = card
        self.surname = surname
        self.name = name
        self.patronymic = patr
        self.programs = pr

class Course(DeclBase):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key = True)
    name = Column(String)

    students = relationship("Student", secondary='marks', back_populates="courses")
    programs = relationship("Program", secondary='programs_courses', back_populates="courses")

    def __init__(self, course_name):
        self.name = course_name
        
class Program(DeclBase):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    name = Column(String)   

    courses = relationship("Course", secondary='programs_courses', back_populates="programs")
    
    def __init__(self, pr_name):
        self.name = pr_name

class StudentCourses(DeclBase):
    __tablename__ = 'marks'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    mark = Column(Integer)

    def __init__(self, mark, st_id, c_id):
        self.student_id = st_id
        self.course_id = c_id
        self.mark = mark

class ProgramCourses(DeclBase):
    __tablename__ = 'programs_courses'

    semester_number = Column(Integer)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    program_id = Column(Integer, ForeignKey('programs.id'), primary_key=True)



# ADD
# создаем программу физика и студента, учащегося на этой программе
# записываем в бд с помощью орм
if False:
    pr1 = Program("Физика")
    st1 = Student('288092', 'Chech', 'Pasha', 'Petrovich', pr1)
    session.add_all(st1, c1)
    session.commit()

# создаем курс "Общая физика. Механика" и добавим его студенту с фамилией Чех. 
# Студента (объект Student) и курс (объект Course) получим с помощью запроса к бд орм 
if False:
    c1 = Course("Общая физика. Механика")

    session.add(c1)
    session.commit()

    st_q = session.query(Student).filter_by(surname='Chech')
    st_id = st_q.id

    c_q = session.query(Course, Course.id).filter_by(name='Общая физика. Механика')
    c_id = c_q.id

    agg = StudentCourses("5", st_id, c_id)

    session.add(agg)
    session.commit()


# UPDATE
# поменяем номер зачетки студента с помощью орм

stud_to_change = session.query(Student, Student.card).filter_by(surname='Chech').first()
print(stud_to_change)
print(stud_to_change.Student.card)          # 288092

stud_to_change.Student.card = '245089'      # 245089
session.commit()


# DELETE
# удалим все программы, связанные с физкультурой из таблицы Programs с помощью орм

fizkult = session.query(Program).filter(Program.name.like('%изкульт%'))

for fiz in fizkult:
    print(fiz.name + " ")


for fiz in fizkult:
    session.delete(fiz)
    session.commit()


# получим список студентов вместе с программами и курсами

query = session.query(Student, Program).join(Program).all()

for (st, pr) in query:
    print(st.surname + " " + st.name + " " + st.card + " " + pr.name)

# посчитаем, сколько в каждой программе содержится курсов

query = session.query(Program.name, func.count(Course.name)).join(ProgramCourses, Program.id == ProgramCourses.program_id).join(Course, ProgramCourses.course_id == Course.id).group_by(Program.name).all()

for (name, amount) in query:
    print("Программа \"" + name + "\" содержит " + str(amount) + " курса")

# посчитаем среднюю оценку по каждому курсу

query = session.query(Course.name, func.avg(StudentCourses.mark))
query = query.join(ProgramCourses, Course.id == ProgramCourses.course_id)
query = query.join(Program, ProgramCourses.program_id == Program.id )
query = query.join(Student, Program.id == Student.program_id)
query = query.join(StudentCourses, Student.id == StudentCourses.student_id)
query = query.group_by(Course.name).all()

for (course, avg_mark) in query:
    print(course + ": " + str(round(avg_mark, 2)))








