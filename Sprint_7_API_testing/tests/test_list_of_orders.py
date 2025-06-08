from Utils.api_methods import APIOrderMethods
import allure


class TestListOfOrders:

    @allure.title("Проверяем, что в тело ответа возвращается список заказов, а код ответа 200")
    def test_get_order_list(self):

        response, status_code = APIOrderMethods.get_orders_list(courier_id="1")
        assert response, "Ответ не вернул список заказов"
        assert status_code == 200, " Статус код должен быть = 200"
