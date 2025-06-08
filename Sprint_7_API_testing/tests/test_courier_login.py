from Utils.api_methods import APICourierMethods
from data.data import Payloads
import pytest
import allure


class TestCourierLogin:

    @allure.title("Проверяем, что курьер может авторизоваться")
    def test_create_courier(self):
        data = Payloads().create_courier_data()
        APICourierMethods.create_courier(data)
        response, status_code = APICourierMethods.login_courier(data)
        assert status_code == 200, "Неуспешная авторизация курьера"
        assert response["id"], "При авторизации не был получен ID"

    @allure.title("Проверяем, что нельзя авторизовать курьера без логина и пароля")
    @pytest.mark.parametrize("data",
                             [
                                 {"login": 'Christopher Cain', "password": ''},
                                 {"login": '', "password": '5504'},
                      
                             ]
                             )
    def test_login_courier_with_missing_login(self, data):
        APICourierMethods.create_courier(data)
        response, status_code = APICourierMethods.login_courier(data)
        assert status_code == 400
        assert response["message"] == "Недостаточно данных для входа"

    
    
    @allure.title("Проверяем, что нельзя авторизовать курьера под несуществующим пользователем или паролем")
    @pytest.mark.parametrize('data', [
        {"login": 'Christopher_UNREAL_99', "password": '5504'},
        {"login": 'Christopher Cain', "password": '115504'}
    ])
    def test_login_courier_with_unreal_login(self, data):
        response, status_code = APICourierMethods.login_courier(data)
        assert status_code == 404
        assert response["message"] == "Учетная запись не найдена"
