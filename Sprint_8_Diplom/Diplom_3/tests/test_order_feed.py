import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage


@allure.story("Проверка раздела «Лента заказов»")
class TestOrderFeed:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_press_order_get_popup(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_orders_feed_button()
        page = OrderFeedPage(browser)
        page.select_last_order()
        assert page.is_order_modal_appear(), "При выборе заказа не появляется окно с деталями"

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_order_displayed_in_feed(self, browser, create_order):
        order_number = f"#0{create_order}"
        page = MainPage(browser)
        page.open()
        page.go_to_orders_feed_button()
        page = OrderFeedPage(browser)
        assert page.find_order_in_order_list(order_number=order_number), f"Заказ {order_number}, не найден"

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_increment_total_orders_counter(self, browser, login_user):
        page = MainPage(browser)
        page.open()
        page.go_to_orders_feed_button()
        page = OrderFeedPage(browser)
        total_orders = page.get_total_orders_number()
        page.go_to_constructor_button()
        page = ConstructorPage(browser)
        page.create_an_order()
        page.go_to_orders_feed_button()
        page = OrderFeedPage(browser)
        new_total_orders = page.get_total_orders_number()

        assert new_total_orders > total_orders, "После создания заказа, общее кол-во заказов не изменилось"

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_increment_today_orders_counter(self, browser, login_user):

        page = MainPage(browser)
        page.open()
        page.go_to_orders_feed_button()
        page = OrderFeedPage(browser)
        total_orders = page.get_today_orders_number()
        page.go_to_constructor_button()
        page = ConstructorPage(browser)
        page.create_an_order()
        page.go_to_orders_feed_button()
        page = OrderFeedPage(browser)
        new_total_orders = page.get_today_orders_number()

        assert new_total_orders > total_orders, "После создания заказа, кол-во заказов за сегодня не изменилось"

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_create_order_get_number_in_work_list(self, browser, login_user):
        page = ConstructorPage(browser)
        order_number = page.create_an_order()
        page.go_to_orders_feed_button()
        page = OrderFeedPage(browser)
        order_in_work = page.get_order_number_in_work_list()

        assert order_number > order_in_work, "Созданный заказ не появился в разделе «В работе»"
