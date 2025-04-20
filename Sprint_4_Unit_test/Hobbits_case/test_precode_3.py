import pytest
from miles import HobbitsPriorityStatus


class TestHobbitsPriorityStatus:

    # добавь параметризацию
    @pytest.mark.parametrize("miles, status", [[299, "Classic"], [300, "Silver"]])
    def test_add_miles_and_check_status(self, miles, status):
        # создай нового хоббита в системе, добавь ему мили и проверь его статус
        hobbits_priority = HobbitsPriorityStatus()
        hobbits_priority.add_new_hobbit("Gollum")
        hobbits_priority.add_miles_to_hobbit("Gollum", miles)
        gollum_status = hobbits_priority.get_status("Gollum")
        assert gollum_status == status, f"Incorrect status:expected {status}, but get {gollum_status}"
