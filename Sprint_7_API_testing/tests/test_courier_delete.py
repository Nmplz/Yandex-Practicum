from Utils.api_methods import APICourierMethods
from data.data import Payloads
import allure


class TestCourierRegister:

    @allure.title("Создаем и потом удаляем курьера. Позитивный сценарий")
    def test_delete_courier(self):
        data = Payloads().create_courier_data()
        APICourierMethods.create_courier(data)
        c_response, c_status_code = APICourierMethods.login_courier(data)
        courier_id = c_response["id"]
        del_response, del_status_code = APICourierMethods.delete_courier(courier_id)

        assert del_status_code == 200, "Неуспешное удаление курьера"
        assert del_response["ok"], "Учетная запись курьера не была удалена"

    @allure.title("Создаем и потом удаляем курьера без ID")
    def test_delete_courier_without_id(self):
        data = Payloads().create_courier_data()
        APICourierMethods.create_courier(data)
        _ , _ = APICourierMethods.login_courier(data)
        del_response, del_status_code = APICourierMethods.delete_courier("")

        assert del_status_code == 404, "Код ответа должен быть 404"
        assert del_response["message"] == "Not Found.", "Учетная запись курьера не должна была удалена"

    @allure.title("Отправка запроса с несуществующим ID")
    def test_delete_courier_without_id(self):
        del_response, del_status_code = APICourierMethods.delete_courier("99999999")

        assert del_status_code == 404, "Код ответа должен быть 404"
        assert del_response["message"] == 'Курьера с таким id нет.'
        
        


