import pytest
from praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_name.return_value = 'Тестовая булка'
    bun_mock.get_price.return_value = 1000
    return bun_mock

@pytest.fixture
def ingredient_mock():
    ingredient_mock = Mock()
    ingredient_mock.get_type.return_value = 'TEST_TYPE'
    ingredient_mock.get_name.return_value = 'TEST_VALUE'
    ingredient_mock.get_price.return_value = 100
    return ingredient_mock