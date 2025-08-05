import allure

from utils.generators import generate_email, generate_name
from faker import Faker


faker = Faker()


class Payloads:

    @staticmethod
    @allure.step("Создание данных пользователя")
    def generate_user_data():
        return {
            "email": generate_email(),
            "password": faker.password(),
            "name": generate_name(),
        }