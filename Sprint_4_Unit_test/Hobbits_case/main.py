class HobbitsPriorityStatus:

    def __init__(self):
        self.hobbits_miles = {'Фродо': 505, 'Сэм': 499, 'Мэри': 350, 'Пиппин': 350}

    def add_new_hobbit(self, hobbit_name):
        self.hobbits_miles[hobbit_name] = 0

    def add_miles_to_hobbit(self, hobbit_name, miles):
        if self.hobbits_miles.get(hobbit_name) is not None:
            self.hobbits_miles[hobbit_name] = miles

    def get_status(self, hobbit_name):
        if not self.hobbits_miles.get(hobbit_name):
            return ''

        if self.hobbits_miles[hobbit_name] < 300:
            return 'Classic'

        if 300 <= self.hobbits_miles[hobbit_name] < 400:
            return 'Silver'

        if 400 <= self.hobbits_miles[hobbit_name] < 500:
            return 'Gold'

        if self.hobbits_miles[hobbit_name] >= 500:
            return 'Platinum'