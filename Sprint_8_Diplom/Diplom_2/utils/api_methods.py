from data.urls import Urls
import requests


class APIUserMethods:

    @staticmethod
    def create_user(payload):
        url = Urls.CREATE_USER_URL
        response = requests.post(
            url,
            data=payload,
        )
        return response.json(), response.status_code

    @staticmethod
    def login_user(payload):
        url = Urls.USER_LOGIN_URL
        response = requests.post(url, json=payload)
        return response.json(), response.status_code

    @staticmethod
    def get_user_data(payload):
        url = Urls.USER_INFO_URL
        response = requests.get(url, json=payload)
        return response.json(), response.status_code

    @staticmethod
    def change_user_data(headers, payload):
        url = Urls.USER_INFO_URL
        response = requests.patch(url, json=payload, headers=headers)
        return response.json(), response.status_code

    @staticmethod
    def delete_user(headers):
        url = Urls.DELETE_USER_URL
        response = requests.delete(url, headers=headers)
        return response.json(), response.status_code


class APIOrderMethods:
    
    @staticmethod
    def create_order(payload):
        url = Urls.CREATE_ORDER_URL
        response = requests.post(url, json=payload)
        return response.json(), response.status_code


    @staticmethod
    def get_ingridients_id():
        url = Urls.GET_INGRIDIENTS_URL
        response = requests.get(url)
        return response.json(), response.status_code
    

    @staticmethod
    def get_all_orders():
        url = Urls.GET_ALL_ORDERS_URL
        response = requests.get(url)
        return response.json(), response.status_code
    
    @staticmethod
    def get_all_user_orders(headers):
        url = Urls.GET_USER_ORDERS_URL
        response = requests.get(url, headers=headers)
        return response.json(), response.status_code
