# 🎓 Автотесты API для [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

Проект автоматизированных тестов для проверки REST API сервиса **Stellar Burgers**.  
Реализованы ключевые сценарии пользовательского взаимодействия с системой — от регистрации до оформления заказа.

---

## ✅ Покрытые сценарии:

🔹 **Создание пользователя** — проверка регистрации с уникальными и дублирующими данными  
🔹 **Авторизация пользователя** — успешный и неуспешный логин  
🔹 **Изменение пользовательских данных** — обновление имени, почты, пароля  
🔹 **Создание заказа** — с авторизацией и без неё  
🔹 **Получение заказов пользователя** — доступ к истории заказов
---

## 🚀 Установка и настройка

```bash
git clone <репозиторий>
cd Diplom_2
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧪 Запуск тестов

Простой запуск:

```bash
pytest
```

С формированием отчёта Allure:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 📁 Структура проекта

```
conftest.py           # Настройки окружения и фикстуры
data/                 # Тестовые данные
tests/                # UI-тесты
utils/                # Вспомогательные утилиты и генераторы
requirements.txt      # Зависимости проекта
pytest.ini            # Конфигурация pytest
allure-results/       # Папка с отчётами allure
```

---

## 📚 Полезные ресурсы

- [Документация pytest](https://docs.pytest.org/)
- [Allure для Python](https://docs.qameta.io/allure/)
- [Шаблон Page Object](https://martinfowler.com/bliki/PageObject.html)