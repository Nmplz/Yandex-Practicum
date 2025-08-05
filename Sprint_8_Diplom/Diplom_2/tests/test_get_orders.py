from utils.api_methods import APIOrderMethods
import allure


class TestGetOrders:

    @allure.title("Получение заказов авторизованный пользователь")
    def test_get_orders_with_auth_user(self, create_unique_user_and_logon):
        data, _ = create_unique_user_and_logon
        access_token = data["accessToken"]
        response, status_code = APIOrderMethods.get_all_user_orders({"Authorization": access_token})
        assert status_code == 200
        assert response["success"] is True
        assert "orders" in response, 'Ответ не содержит списка заказов'

    @allure.title("Получение заказов неавторизованный  пользователь")
    def test_get_orders_with_no_auth_user(self):
        response, status_code = APIOrderMethods.get_all_user_orders({"Authorization": ''})
        assert status_code == 401
        assert response["success"] == False
        assert response["message"] == 'You should be authorised'

