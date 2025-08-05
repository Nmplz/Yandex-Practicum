from data.data import Payloads
from utils.api_methods import APIUserMethods
import allure


class TestLoginUser:

    @allure.title("логин под существующим пользователем")
    def test_valid_data_user_logon(self, create_unique_user_and_logon):
        login_response, status_code = create_unique_user_and_logon
        assert status_code == 200
        assert login_response["success"] is True
        assert "accessToken" in login_response
        assert "refreshToken" in login_response


    @allure.title("логин с неверным логином или паролем")
    def test_invalid_data_user_logon(self):
        data = Payloads.generate_user_data()
        APIUserMethods.create_user(data)
        login_response, status_code = APIUserMethods.login_user({"email": data["email"], "password": 'invalid_password'})
        assert status_code == 401
        assert login_response["success"] == False
        assert login_response["message"] == 'email or password are incorrect'
