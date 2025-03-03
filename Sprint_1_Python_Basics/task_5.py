class TestCase:
    def __init__(self):
        self.steps = {}
        self.result = None

    def set_step(self, step_number, step_text):
        if isinstance(step_number, int) and isinstance(step_text, str):
            self.steps[step_number] = step_text
        else:
            print("Ошибка типа данных")

    def delete_step(self, step_number):
        if step_number in self.steps:
            del self.steps[step_number]
        else:
            print(f"Шага {step_number} нет.")

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        test_case = {"Шаги": self.steps, "Ожидаемый результат": self.result}
        print(test_case)


test_case_1 = TestCase()
test_case_1.set_step(1, "Перейти на сайт")
test_case_1.set_step(3, "Перейти в раздел Товары")
test_case_1.delete_step(3)
test_case_1.set_step(2, "Перейти в раздел Товары")
test_case_1.set_step(3, "Нажать кнопку «В корзину» у первого товара")
test_case_1.set_result("Товар окажется в корзине")
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, "Перейти на сайт")
test_case_2.set_step(2, "Перейти в раздел Корзина")
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result("Товар удален из корзины")
test_case_2.get_test_case()
