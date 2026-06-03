
from Recipe import Recipe
from Ingredient import Ingredient
from ShoppingList import ShoppingList

import pytest


def test_add_recipe0():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe = Recipe("Салат", [flour, tomato, eggplant])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe, 4.0)
    result = shopping_list.get_list()
    assert result[0]._name == "Баклажан"
    assert result[0].quantity == 1200.0
    assert result[0]._unit == "г"
    assert result[1]._name == "Кукурузный крахмал"
    assert result[1].quantity == 120.0
    assert result[1]._unit == "г"
    assert result[2]._name == "Помидоры"
    assert result[2].quantity == 800.0
    assert result[2]._unit == "г"


def test_add_recipe1():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe = Recipe("Салат", [flour, tomato, eggplant])
    shopping_list = ShoppingList()
    with pytest.raises(ValueError) as exc_info:
        shopping_list.add_recipe(recipe, -4.0)
    assert str(exc_info.value) == "Количество порций должно быть положительным"


def test_remove_recipe0():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe = Recipe("Салат", [flour, tomato, eggplant])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe, 1.0)
    title = "Салат"
    shopping_list.remove_recipe(title)
    assert len(shopping_list.get_list()) == 0


def test_remove_recipe1():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe = Recipe("Салат", [flour, tomato, eggplant])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe, 1.0)
    title = "Завтрак"
    shopping_list.remove_recipe(title)
    assert len(shopping_list.get_list()) == 3


def test_get_list1():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe1 = Recipe("Салат", [flour, tomato, eggplant])
    flour = Ingredient("Кукурузный крахмал", 60.0, "г")
    recipe2 = Recipe("Салат с крахмалом", [flour, tomato, eggplant])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe1, 1.0)
    shopping_list.add_recipe(recipe2, 1.0)
    result = shopping_list.get_list()
    assert result[1].quantity == 90.0


def test_get_list2():
    flour = Ingredient("А", 30.0, "г")
    tomato = Ingredient("Б", 200.0, "г")
    eggplant = Ingredient("В", 300.0, "г")
    recipe1 = Recipe("Салат", [flour, tomato, eggplant])
    flour = Ingredient("А", 60.0, "г")
    recipe2 = Recipe("Салат с крахмалом", [flour])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe1, 1.0)
    shopping_list.add_recipe(recipe2, 1.0)
    result = shopping_list.get_list()
    assert result[1]._name == "Б"
    assert result[0]._name == "А"
    assert result[2]._name == "В"


def test_add():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe1 = Recipe("Салат", [flour, tomato, eggplant])
    flour = Ingredient("Кукурузный крахмал", 60.0, "г")
    recipe2 = Recipe("Салат с крахмалом", [flour])
    shopping_list1 = ShoppingList()
    shopping_list2 = ShoppingList()
    shopping_list1.add_recipe(recipe1, 1.0)
    shopping_list2.add_recipe(recipe2, 1.0)
    fullList = ShoppingList()
    fullList = shopping_list1 + shopping_list2
    result = fullList.get_list()
    assert len(fullList.get_list()) == 3
    assert result[0]._name == "Баклажан"
    assert result[0].quantity == 300.0

    assert result[1]._name == "Кукурузный крахмал"
    assert result[1].quantity == 90.0

    assert result[2]._name == "Помидоры"
    assert result[2].quantity == 200.0
    assert len(shopping_list1.get_list()) == 3
    assert len(shopping_list2.get_list()) == 1
