import requests

from data.urls import Urls



class APIUserMethods:

    @staticmethod
    def create_user(payload):
        url = Urls.CREATE_USER_URL
        response = requests.post(url, data=payload)
        return response.json(), response.status_code

    @staticmethod
    def delete_user(headers):
        url = Urls.DELETE_USER_URL
        response = requests.delete(url, headers=headers)
        return response.json(), response.status_code