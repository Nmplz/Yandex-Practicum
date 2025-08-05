import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [("white bun", 100.0), ("black bun", 150.5), ("golden bun", 999.99)])
def test_bun_properties(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price 
