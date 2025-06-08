from Utils.api_methods import APIOrderMethods, APICourierMethods
from data.data import Payloads
import allure


class TestGetOrderByNuber:

    @allure.title("Получить заказ по его номеру. Успешный запрос возвращает объект с заказом")
    def test_accept_order_with_incorrect_order_id(self):

        order_response, _ = APIOrderMethods.create_order(Payloads().create_single_order_data())
        track = order_response["track"]
        order_info, status_code = APIOrderMethods.get_order_by_track(track)
        assert status_code == 200
        assert order_info['order']

    @allure.title("Запрос без номера заказа возвращает ошибку")
    def test_accept_order_with_incorrect_order_id(self):

        order_info, status_code = APIOrderMethods.get_order_by_track('')
        assert status_code == 400
        assert order_info['message'] == 'Недостаточно данных для поиска'

    @allure.title("Запрос без номера заказа возвращает ошибку")
    def test_accept_order_with_incorrect_order_id(self):

        order_info, status_code = APIOrderMethods.get_order_by_track('999999')
        assert status_code == 404
        assert order_info['message'] == 'Заказ не найден'

