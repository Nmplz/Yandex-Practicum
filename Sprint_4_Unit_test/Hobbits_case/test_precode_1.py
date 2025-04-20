import pytest

# импортируем класс HobbitsPriorityStatus из файла miles.py
from miles import HobbitsPriorityStatus


class TestHobbitsPriorityStatus:

    @pytest.mark.parametrize("hobbit, priority_status", [["Фродо", "Platinum"], ["Сэм", "Gold"], ["Мэри", "Silver"], ["Пиппин", "Silver"]])
    def test_priority_status(self, hobbit, priority_status):  # передай параметры из декоратора в функцию
        assert HobbitsPriorityStatus().get_status(hobbit) == priority_status
