import pytest

# импортируем класс HobbitsPriorityStatus из файла miles.py
from miles import HobbitsPriorityStatus

class TestHobbitsPriorityStatus:

    # добавь декоратор
    ...
    def test_priority_status(self, ...): # передай параметры из декоратора в функцию
        assert HobbitsPriorityStatus().get_status(hobbit) == priority_status
