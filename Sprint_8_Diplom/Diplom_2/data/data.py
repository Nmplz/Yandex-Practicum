from utils.generators import generate_unique_email, generate_unique_name
from faker import Faker
import allure

faker = Faker()


class Payloads:

    @staticmethod
    @allure.step("Создание данных пользователя")
    def generate_user_data():
        return {
            "email": generate_unique_email(),
            "password": faker.password(),
            "name": generate_unique_name(),
        }

    @staticmethod
    @allure.step("Создание пользователя и не заполнить одно из обязательных полей")
    def generate_invalid_user_data():
        return [
            {
                "email": faker.email(),
                "name": faker.name(),
            },
            {
                "email": faker.email(),
                "password": faker.password(),
            },
            {
                "password": faker.password(),
                "name": faker.name(),
            },
        ]

    @staticmethod
    @allure.step('Создание параметров для изменения данных пользователя')
    def get_user_update_parameters():
        return [
            {"name" :generate_unique_name()},
            {"email": generate_unique_email()},
            {"password": "newpass12345"}
        ]