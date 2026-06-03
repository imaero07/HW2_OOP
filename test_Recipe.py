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
def test_scale():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    recipe = Recipe("Салат", [flour, tomato])
    newRecipe = recipe.scale(2.0)
    assert newRecipe is not recipe
    assert newRecipe._ingredients[0].quantity == 60.0
    assert newRecipe._ingredients[1].quantity == 400.0
    assert recipe._ingredients[0].quantity == 30.0

def test_len():
    flour = Ingredient("Кукурузный крахмал", 30.0, "г")
    tomato = Ingredient("Помидоры", 200.0, "г")
    eggplant = Ingredient("Баклажан", 300.0, "г")
    recipe = Recipe("Салат", [flour, tomato, eggplant])
    assert len(recipe) == 3



