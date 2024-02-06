from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.utils.database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    lessons = relationship("Lesson", back_populates="course")

class Lesson(Base):
    __tablename__ = 'lessons'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))

    course = relationship("Course", back_populates="lessons")
    questions = relationship("Question", back_populates="lesson")

# Asociación muchos a muchos entre preguntas y opciones
question_option_association = Table('question_option_association', Base.metadata,
    Column('question_id', Integer, ForeignKey('questions.id')),
    Column('option_id', Integer, ForeignKey('options.id'))
)

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    question_type = Column(String)  # Tipo de pregunta: boolean, single_answer, multiple_answers, all_or_nothing_multiple
    options = relationship("Option", secondary=question_option_association, back_populates="questions")

class Option(Base):
    __tablename__ = 'options'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    questions = relationship("Question", secondary=question_option_association, back_populates="options")