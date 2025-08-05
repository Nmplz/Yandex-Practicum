import pytest
from data.data import Payloads
from utils.api_methods import APIUserMethods


@pytest.fixture
def create_unique_user_and_logon():
    data = Payloads.generate_user_data()
    APIUserMethods.create_user(data)
    login_response, status_code = APIUserMethods.login_user({"email": data["email"], "password": data["password"]})
    yield login_response, status_code
    APIUserMethods.delete_user(headers={"Authorization": login_response["accessToken"]})


@pytest.fixture
def create_unique_user():
    data = Payloads.generate_user_data()
    response, status_code = APIUserMethods.create_user(data)
    yield response, status_code
    APIUserMethods.delete_user(headers={"Authorization": response["accessToken"]})
