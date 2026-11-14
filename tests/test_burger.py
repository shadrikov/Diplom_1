import pytest
from praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:
    # Метод set_buns: передан правильный объект (мок булки)
    def test_set_buns_correct_object_passed(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    # Метод add_ingredient: ингредиент успешно добавляется в список
    def test_add_ingredient_ingredient_appends_to_list(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients == [ingredient_mock]

    # Метод remove_ingredient: ингредиент успешно удаляется из списка по индексу
    def test_remove_ingredient_ingredient_removes_by_index_successful(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    # Метод move_ingredient: ингредиент успешно перемещается в списке с первого на последнее место
    def test_move_ingredient_ingredient_moves_from_first_to_last_position_successful(self, burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_3 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient_2, ingredient_3, ingredient_1]

    # Метод get_price: разные комбинации ингредиентов и булочек дают корректную стоимость бургера (параметризация)
    @pytest.mark.parametrize('bun_price, ingredient_prices, total_price', [
        (1255, [80], 2590),      # Булка х2 и один ингредиент
        (988, [90, 3000], 5066), # Булка х2 и два ингредиента
        (1255, [], 2510),        # Только булка х2
        (0, [15], 15)            # Только ингредиент
    ])
    def test_get_price_various_bun_and_ingredients_returns_correct_total(self, burger, bun_price, ingredient_prices, total_price):
        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        burger.set_buns(bun_mock)
        for price in ingredient_prices:
            ingredient_mock = Mock()
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == total_price

    # Метод get_receipt: информация в чеке соответствует ожидаемой
    def test_get_receipt_receipt_text_matches_expected_text(self, burger, bun_mock, ingredient_mock):
        burger.set_buns(bun_mock)
        ingredient_2 = Mock()
        ingredient_2.get_type.return_value = 'TEST_TYPE_2'
        ingredient_2.get_name.return_value = 'TEST_VALUE_2'
        ingredient_2.get_price.return_value = 50
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(ingredient_2)
        expected_text = (
            '(==== Тестовая булка ====)\n'
            '= test_type TEST_VALUE =\n'
            '= test_type_2 TEST_VALUE_2 =\n'
            '(==== Тестовая булка ====)\n'
            '\n'
            'Price: 2150'
        )
        assert burger.get_receipt() == expected_text