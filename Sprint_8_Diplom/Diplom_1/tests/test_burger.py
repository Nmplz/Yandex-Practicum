from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_burger_set_bun_and_price():
    bun = Mock(Bun)
    bun.get_price.return_value = 100
    burger = Burger()
    burger.set_buns(bun)
    assert burger.get_price() == 200


def test_burger_add_ingredient():
    burger = Burger()
    mock_ingredient = Mock(Ingredient)
    mock_ingredient.get_price.return_value = 50
    burger.set_buns(Mock(get_price=Mock(return_value=100)))
    burger.add_ingredient(mock_ingredient)
    assert burger.get_price() == 250


def test_burger_remove_ingredient():
    burger = Burger()
    ing1 = Mock(Ingredient)
    ing2 = Mock(Ingredient)
    burger.ingredients = [ing1, ing2]
    burger.remove_ingredient(0)
    assert burger.ingredients == [ing2]


def test_burger_move_ingredient():
    burger = Burger()
    ing1 = Mock(Ingredient)
    ing2 = Mock(Ingredient)
    burger.ingredients = [ing1, ing2]
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ing2, ing1]


def test_get_receipt():
    bun = Mock()
    bun.get_name.return_value = "TestBun"
    bun.get_price.return_value = 100

    ing = Mock()
    ing.get_name.return_value = "TestIngredient"
    ing.get_price.return_value = 50
    ing.get_type.return_value = "SAUCE"

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ing)

    receipt = burger.get_receipt()

    assert "TestBun" in receipt
    assert "TestIngredient" in receipt
    assert "Price: 250" in receipt

