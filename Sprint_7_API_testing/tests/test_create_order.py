from Utils.api_methods import APIOrderMethods
from data.data import Payloads
import pytest
import json
import allure


class TestCreateOrder:

    @allure.title("Проверяем, что при создании можно указать: один цвет, оба цвета, без цвета. Ответ содержит track_ID")
    @pytest.mark.parametrize("data", Payloads().create_multiple_order_data())
    def test_create_order(self, data):

        user_data = json.dumps(data)
        response, status_code = APIOrderMethods.create_order(user_data)

        assert status_code == 201, "Неправильный статус код"
        assert response["track"], "TRACK не был передан в ответ"
