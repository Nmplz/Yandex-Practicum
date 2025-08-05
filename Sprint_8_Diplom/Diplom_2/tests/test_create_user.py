from data.data import Payloads
from utils.api_methods import APIUserMethods
import pytest
import allure


class TestCreateUser:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self, create_unique_user):
        response, status_code = create_unique_user
        assert response["success"], "Пользователь не создан"
        assert status_code == 200

    @allure.title("Создать пользователя и не заполнить одно из обязательных полей")
    @pytest.mark.parametrize("data", Payloads.generate_invalid_user_data())
    def test_create_user_with_invalid_data(self, data):
        response, status_code = APIUserMethods.create_user(data)
        assert status_code == 403
        assert response["success"] == False, "Пользователь не должен быть создан"
        assert response["message"] == "Email, password and name are required fields"

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_duplicate_user(self):
        data = Payloads.generate_user_data()
        APIUserMethods.create_user(data)
        response, status_code = APIUserMethods.create_user(data)
        assert status_code == 403
        assert response["success"] == False, "Сущестующий пользователь не должен быть создан"
        assert response["message"] == "User already exists"
