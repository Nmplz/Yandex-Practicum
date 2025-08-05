from utils.api_methods import APIOrderMethods
import allure


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, create_unique_user_and_logon):
        ing_list = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
        make_order_response, status_code = APIOrderMethods.create_order(ing_list)
        assert status_code == 200
        assert make_order_response["success"] is True
        assert make_order_response["name"] == "Метеоритный флюоресцентный бургер"
 


    @allure.title("Создание заказа без авторизации")
    def test_create_order_no_auth(self):

        ing_list = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
        make_order_response, status_code = APIOrderMethods.create_order(ing_list)
        assert status_code == 200
        assert make_order_response["success"] is True
        assert make_order_response["name"] == "Метеоритный флюоресцентный бургер"


    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingridients(self):
        ing_list = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
        make_order_response, status_code = APIOrderMethods.create_order(ing_list)
        assert status_code == 200
        assert make_order_response["success"] is True
        assert make_order_response["name"] == "Метеоритный флюоресцентный бургер"

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingridients(self):
        ing_list = {"ingredients": []}
        make_order_response, status_code = APIOrderMethods.create_order(ing_list)
        assert status_code == 400
        assert make_order_response["success"] is False
        assert make_order_response["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingridients_hash(self):
        ing_list = {"ingredients": ["60d3463f7034a000269f45e1", "60d3463f7034a000269f45e9"]}
        make_order_response, status_code = APIOrderMethods.create_order(ing_list)
        assert status_code == 400
        assert make_order_response["success"] == False
        assert make_order_response["message"] == "One or more ids provided are incorrect"
                

