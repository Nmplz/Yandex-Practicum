import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {"чипсы": 50, "кола": 100, "печенье": 45, "молоко": 55, "кефир": 70}
        self.__tax_rate = {"чипсы": 20, "кола": 20, "печенье": 20, "молоко": 10, "кефир": 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if not 0 < len(name) < 41:
            raise ValueError("Нельзя добавить товар, если в его названии нет символов или их больше 40")
        elif name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name in self.__name_items:
            self.__name_items.remove(name)
            self.__number_items -= 1
        else:
            raise NameError("Позиция отсутствует в чеке")

    @staticmethod
    def is_discount_available(items: list) -> bool:
        return len(items) > 10

    def check_amount(self):
        total = []
        for item_name in self.__name_items:
            total.append(self.__item_price[item_name])

        if self.is_discount_available(total):
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item_name in self.__name_items:
            if self.__tax_rate[item_name] == 20:
                twenty_percent_tax.append(item_name)
                total.append(self.__item_price[item_name])

        if self.is_discount_available(self.__name_items):
            return sum(total) * 0.2 * 0.9
        else:
            return sum(total) * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item_name in self.__name_items:
            if self.__tax_rate[item_name] == 10:
                ten_percent_tax.append(item_name)
                total.append(self.__item_price[item_name])

        if self.is_discount_available(self.__name_items):
            return sum(total) * 0.1 * 0.9
        else:
            return sum(total) * 0.1

    def total_tax(self):
        total_tax_amount = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return total_tax_amount

    @staticmethod
    def get_telephone_number(telephone_number: int) -> str:
        if not isinstance(telephone_number, int):
            raise ValueError("Необходимо ввести цифры")
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f"+7{str(telephone_number)}"

    @staticmethod
    def get_date_and_time() -> list:
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ["year", lambda x: x.year],
            ["month", lambda x: x.month],
            ["day", lambda x: x.day],
            ["hour", lambda x: x.hour],
            ["minute", lambda x: x.minute],
        ]

        date_and_time = [f"{name}:{func(now)}" for name, func in date]
        return date_and_time
