# Sprint 7 — API Testing Framework 🚀

Проект автоматизации тестирования API для сервиса заказа самокатов.

## 📦 Структура проекта

```
Sprint_7/
├── Utils/                 # API методы
│   └── api_methods.py     # Методы для курьеров и заказов
├── tests/                 # Набор автотестов
│   ├── test_courier_create.py
│   ├── test_courier_login.py
│   └── ... и другие
├── data/                  # Дополнительные данные (payloads, URLs)
├── pytest.ini             # Настройки Pytest
├── requirements.txt       # Зависимости проекта
└── README.md              # Этот файл
```

## 🧪 Тестируемые сценарии

- ✅ Создание курьера
- ✅ Авторизация курьера
- ✅ Удаление курьера
- ✅ Создание заказа
- ✅ Получение списка заказов
- ✅ Привязка заказа к курьеру

## 🚀 Запуск тестов

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов
pytest -v

# С Allure-отчётом
pytest --alluredir=allure-results
allure serve allure-results
```

## 🛠 Используемые технологии

- `Python 3.10+`
- `Pytest`
- `Allure`
- `Faker` — для генерации данных


**Автор:** Nmplz  
Учебный проект в рамках Sprint 7 Яндекс.Практикума
