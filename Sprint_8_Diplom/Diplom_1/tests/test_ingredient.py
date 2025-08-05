import pytest
from praktikum.ingredient import Ingredient


@pytest.mark.parametrize(
    "type_, name, price",
    [
        ("sauce", "ketchup", 30.0),
        ("filling", "cutlet", 120.5),
    ],
)
def test_ingredient_properties(type_, name, price):
    ing = Ingredient(type_, name, price)
    assert ing.get_type() == type_
    assert ing.get_name() == name
    assert ing.get_price() == price
