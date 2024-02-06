from typing import List, Optional, Union
from pydantic import BaseModel

class CourseBase(BaseModel):
    name: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True

class LessonBase(BaseModel):
    title: str
    content: Optional[str] = None
    course_id: int

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    text: str

class BooleanQuestionCreate(QuestionBase):
    correct_answer: bool

class MultipleChoiceSingleAnswerQuestionCreate(QuestionBase):
    options: List[str]
    correct_answer: str

class MultipleChoiceMultipleAnswersQuestionCreate(QuestionBase):
    options: List[str]
    correct_answers: List[str]

class AllOrNothingMultipleChoiceQuestionCreate(QuestionBase):
    options: List[str]
    correct_answers: List[str]

QuestionCreate = Union[BooleanQuestionCreate, MultipleChoiceSingleAnswerQuestionCreate, 
                        MultipleChoiceMultipleAnswersQuestionCreate, AllOrNothingMultipleChoiceQuestionCreate]

class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True
