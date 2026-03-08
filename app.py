from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from models import User, UserAge, Feedback

# Создаем экземпляр приложения
app = FastAPI()

# --- Задание 1.1 ---
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}
    # Для проверки авторелоада поменяй текст на "Авторелоад действительно работает" и сохрани файл.

# --- Задание 1.2 ---
@app.get("/html")
def read_html():
    return FileResponse("index.html")

# --- Задание 1.3* ---
@app.post("/calculate")
def calculate(num1: int = Body(...), num2: int = Body(...)):
    # Принимаем два числа из тела JSON запроса
    return {"result": num1 + num2}

# --- Задание 1.4 ---
# Создаем экземпляр класса User
default_user = User(name="Иван Иванов", id=1)

@app.get("/users")
def get_user():
    return default_user

# --- Задание 1.5* ---
@app.post("/user")
def check_adult(user: UserAge):
    # Проверяем возраст
    is_adult = user.age >= 18
    # Возвращаем те же данные + новое поле
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

# --- Задание 2.1 и 2.2* ---
# Хранилище (список) для отзывов
feedbacks =[]

@app.post("/feedback")
def post_feedback(feedback: Feedback):
    # При успехе сохраняем данные в список
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}