# 🧪 Sprint_5: Автоматизация тестирования веб-приложения

Проект по автоматизации тестирования веб-приложения с использованием фреймворков **Pytest** и **Selenium WebDriver**.  
Реализован шаблон **Page Object Model (POM)**, обеспечивающий читаемость, переиспользуемость и лёгкость поддержки тестов.

---

## 📁 Структура проекта

```
Sprint_5/
├── pages/                         # Page Object модели
│   ├── base_page.py              # Общая логика взаимодействия с элементами
│   ├── main_page.py              # Главная страница
│   └── registration_modal.py     # Модальное окно входа/регистрации
├── tests/                         # Тестовые сценарии
│   ├── test_authentication.py
│   └── test_place_advertisement.py
├── utils/                         # Вспомогательные модули
│   └── generators.py              # Генерация случайных email и других данных
├── conftest.py                    # Фикстуры и конфигурации Pytest
├── requirements.txt               # Зависимости проекта
└── pytest.ini                     # Конфигурация запуска Pytest
```

---

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Запуск тестов

Запуск всех тестов:

```bash
pytest
```

Запуск тестов с определённым маркером:

```bash
pytest -m place_ad
```

### 3. Примеры использования

- Авторизация и проверка отображения профиля
- Проверка недоступности размещения объявления без авторизации
- Проверка появления модального окна при нажатии на кнопку входа
- Валидация данных в карточке объявления: название, цена, город

---

## 🧰 Технологии

- [Python 3.10+](https://www.python.org/)
- [Selenium WebDriver](https://www.selenium.dev/)
- [Pytest](https://docs.pytest.org/en/latest/)
- [Page Object Model](https://martinfowler.com/bliki/PageObject.html)

---

## 🏷 Маркеры Pytest

В `pytest.ini` зарегистрированы кастомные маркеры:

- `@pytest.mark.registration_form` — тесты регистрации и авторизации
- `@pytest.mark.place_ad` — тесты размещения объявления

---

