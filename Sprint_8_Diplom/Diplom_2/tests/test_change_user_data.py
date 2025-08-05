from data.data import Payloads
from utils.api_methods import APIUserMethods
import pytest
import allure


class TestChangeUserData:

    @allure.title("Изменение данных пользователя с авторизацией")
    @pytest.mark.parametrize("upd_data", Payloads.get_user_update_parameters())
    def test_change_user_data_with_auth(self, upd_data, create_unique_user_and_logon):
        login_response, status_code = create_unique_user_and_logon
        access_token = login_response["accessToken"]
        headers = {"Authorization": access_token}
        changed_data_response, status_code = APIUserMethods.change_user_data(headers=headers, payload=upd_data)

        assert status_code == 200
        assert changed_data_response["success"] is True

    @allure.title("Изменение данных пользователя без авторизации")
    @pytest.mark.parametrize("upd_data", Payloads.get_user_update_parameters())
    def test_change_user_data_without_auth(self, upd_data):
        changed_data_response, status_code = APIUserMethods.change_user_data(headers={"Authorization": ""}, payload=upd_data)

        assert status_code == 401
        assert changed_data_response["success"] == False
        assert changed_data_response["message"] == "You should be authorised"
