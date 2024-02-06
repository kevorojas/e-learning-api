from fastapi import FastAPI
from app.utils.database import engine, Base
from app.controllers import courses, lessons, questions

app = FastAPI()

# Crear las tablas al iniciar la aplicación
Base.metadata.create_all(bind=engine)

# Incluir las rutas de los controladores
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
app.include_router(questions.router, prefix="/questions", tags=["questions"])
