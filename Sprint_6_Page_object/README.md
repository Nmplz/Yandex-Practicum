# 🛴 Автотесты для сервиса аренды самокатов

Проект содержит автоматизированные UI-тесты для сайта [qa-scooter.praktikum-services.ru](https://qa-scooter.praktikum-services.ru), написанные с использованием `Selenium`, `pytest` и `Allure`.

## 📦 Технологии

- Python 3.10+
- Selenium WebDriver
- Pytest
- Allure Report
- Page Object Model (POM)
- JSON-параметризация тестов

---

## 🚀 Как запустить тесты

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Запустить тесты

```bash
pytest --alluredir=allure-results
```

### 3. Посмотреть Allure-отчёт

```bash
allure serve allure-results
```

или:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## 🧪 Структура проекта

```
.
├── pages/              # Page Object модели (MainPage, OrderPage и т.д.)
├── locators/           # Локаторы элементов
├── tests/              # Тестовые сценарии
├── utils/              # Утилиты (например, data_loader)
├── test_data/          # JSON-файлы с тестовыми данными
├── conftest.py         # Фикстуры и конфигурации pytest
├── requirements.txt
└── README.md
```

---

## 📚 Покрытие тестами

- Проверка FAQ на главной странице
- Переходы по кнопкам «Заказать»
- Проверка перехода по логотипам (Яндекс и Самокат)
- Полный позитивный сценарий оформления заказа
- Параметризация формы заказа (через JSON)

---

## 🧑‍💻 Запуск отдельных тестов

```bash
pytest tests/test_order_form.py::TestOrderForm::test_place_test_order
```

---

## 📌 Примечания

- Для корректной работы Allure CLI должен быть установлен и добавлен в `PATH`
- Все действия описаны через `@allure.step` и `@allure.title` для удобной навигации в отчёте

---

