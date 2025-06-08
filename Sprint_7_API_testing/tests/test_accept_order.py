from Utils.api_methods import APIOrderMethods, APICourierMethods
from data.data import Payloads
import allure


class TestAcceptOrder:

    @allure.title("Принятие заказа. Позитивный сценарий")
    def test_accept_order(self):

        courier_data = Payloads().create_courier_data()
        APICourierMethods.create_courier(courier_data)

        order_response, _ = APIOrderMethods.create_order(Payloads().create_single_order_data())
        track = order_response["track"]

        order_info, _ = APIOrderMethods.get_order_by_track(track)
        order_id = order_info["order"]["id"]

        courier_response, _ = APICourierMethods.login_courier(courier_data)
        courier_id = courier_response["id"]

        accept_response, status_code = APIOrderMethods.put_order_to_courier(courier_id, order_id)

        assert status_code == 200
        assert accept_response["ok"]

    @allure.title("Принятие заказа. Если передать несуществующий id курьера, запрос вернёт ошибку ")
    def test_accept_order_with_unvalid_id(self):

        order_response, _ = APIOrderMethods.create_order(Payloads().create_single_order_data())
        track = order_response["track"]

        order_info, _ = APIOrderMethods.get_order_by_track(track)
        order_id = order_info["order"]["id"]

        accept_response, status_code = APIOrderMethods.put_order_to_courier("99999999", order_id)

        assert status_code == 404
        assert accept_response["message"] == "Курьера с таким id не существует"

    @allure.title("Принятие заказа. Если не передать  id курьера, запрос вернёт ошибку ")
    def test_accept_order_with_no_courier_id(self):

        order_response, _ = APIOrderMethods.create_order(Payloads().create_single_order_data())
        track = order_response["track"]

        order_info, _ = APIOrderMethods.get_order_by_track(track)
        order_id = order_info["order"]["id"]

        accept_response, status_code = APIOrderMethods.put_order_to_courier("", order_id)

        assert status_code == 400
        assert accept_response["message"] == "Недостаточно данных для поиска"

    @allure.title("Принятие заказа. Если не передать  id заказа, запрос вернёт ошибку ")
    def test_accept_order_with_no_order_id(self):

        courier_data = Payloads().create_courier_data()
        APICourierMethods.create_courier(courier_data)

        courier_response, _ = APICourierMethods.login_courier(courier_data)
        courier_id = courier_response["id"]

        accept_response, status_code = APIOrderMethods.put_order_to_courier(courier_id, "")

        assert status_code == 404
        assert accept_response["message"] == "Not Found."

    @allure.title("Принятие заказа. Если передать неверный id заказа, запрос вернёт ошибку ")
    def test_accept_order_with_incorrect_order_id(self):

        courier_data = Payloads().create_courier_data()
        APICourierMethods.create_courier(courier_data)

        courier_response, _ = APICourierMethods.login_courier(courier_data)
        courier_id = courier_response["id"]

        accept_response, status_code = APIOrderMethods.put_order_to_courier(courier_id, "9999999")

        assert status_code == 404
        assert accept_response["message"] == "Заказа с таким id не существует"
