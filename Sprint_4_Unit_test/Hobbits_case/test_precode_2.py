import pytest
from miles import HobbitsPriorityStatus


class TestHobbitsPriorityStatus:

    def test_add_miles_and_check_status(self):

        hobbits_priority = HobbitsPriorityStatus()
        hobbits_priority.add_new_hobbit("Gollum")
        hobbits_priority.add_miles_to_hobbit("Gollum", 50)
        gollum_status = hobbits_priority.get_status("Gollum")
        assert gollum_status == "Classic", "Неправильно начислен статус"
