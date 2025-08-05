# 🧪 Diplom_3

Автотесты для проверки веб-приложения [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
---

## 🚀 Быстрый старт

### 1. Клонируй репозиторий и установи зависимости

```bash
git clone https://github.com/Nmplz/Diplom_3.git
cd Diplom_3
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
```

### 2. Запуск тестов

```bash
pytest -m restore_password --alluredir=reports/allure
```

### 3. Просмотр отчета Allure

```bash
allure serve reports/allure
```

---

## 📁 Структура проекта

```
pages/                   # Page Object модели
locators/                # Селекторы
tests/                   # pytest тесты
fixtures/                # Фикстуры (например, браузер, данные)
utils/                   # Вспомогательные функции и генераторы
conftest.py              # Общие настройки и фикстуры pytest
requirements.txt         # Зависимости проекта
pytest.ini               # Конфигурация pytest
```

---

## 📚 Полезные ссылки

- [Документация pytest](https://docs.pytest.org/)
- [Документация Allure](https://docs.qameta.io/allure/)
- [Page Object Pattern](https://martinfowler.com/bliki/PageObject.html)