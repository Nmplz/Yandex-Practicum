from data.urls import Urls
import requests


class APICourierMethods:

    @staticmethod
    def create_courier(payload):
        url = Urls.COURIER_URL

        response = requests.post(
            url,
            data=payload,
        )
        return response.json()

    @staticmethod
    def login_courier(payload):
        url = Urls.COURIER_LOGIN_URL

        response = requests.post(
            url,
            data=payload,
        )
        return response.json(), response.status_code

    @staticmethod
    def delete_courier(courier_id):
        url = f"{Urls.COURIER_URL}/{courier_id}"
        response = requests.delete(url)
        return response.json(), response.status_code


class APIOrderMethods:

    @staticmethod
    def create_order(payload):
        url = Urls.ORDER_URL

        response = requests.post(
            url,
            data=payload,
        )
        return response.json(), response.status_code

    @staticmethod
    def get_orders_list():
        url = Urls.ORDER_URL
        response = requests.get(url)
        return response.json(), response.status_code

    @staticmethod
    def get_order_by_track(track):
        url = f"{Urls.ORDER_URL}/track?t={track}"
        response = requests.get(url)
        return response.json(), response.status_code

    @staticmethod
    def put_order_to_courier(cour_id, order_id):
        url = f'{Urls.ACCEPT_ORDER_URL}/{order_id}?courierId={cour_id}'
        response = requests.put(url)
        return response.json(), response.status_code
