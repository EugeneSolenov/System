from pydantic import BaseModel, Field, field_validator

# --- Задание 1.4 ---
class User(BaseModel):
    name: str
    id: int

# --- Задание 1.5* ---
class UserAge(BaseModel):
    name: str
    age: int

# --- Задание 2.1 и 2.2* ---
class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    # Кастомная валидация для Pydantic 2.0+
    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, value: str) -> str:
        # Приводим к нижнему регистру для поиска в любых падежах
        lower_val = value.lower()
        forbidden_words = ["кринж", "рофл", "вайб"]
        
        for word in forbidden_words:
            if word in lower_val:
                # Если найдено недопустимое слово, выбрасываем ошибку
                raise ValueError("Использование недопустимых слов")
        return value