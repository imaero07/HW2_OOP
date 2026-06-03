import pytest
from Recipe import Recipe
from Ingredient import Ingredient
def test_init():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe = Recipe("Салат", [flour, tomato, eggplant])
    assert recipe._title == "Салат"
    assert len(recipe._ingredients) == 3
def test_addIngredient0():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    recipe = Recipe("Салат", [flour, tomato])
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe.add_ingredient(eggplant)
    assert eggplant in recipe._ingredients
    assert len(recipe._ingredients)==3
def test_addIngredient1():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    recipe = Recipe("Салат", [flour, tomato])
    recipe.add_ingredient(tomato)
    assert tomato.quantity==400.0


