import pytest
from Ingredient import Ingredient
def test_quantity():
    with pytest.raises(ValueError):
        Ingredient("Кукурузный крахмал", -0.5, "ц")
def test__str__():
    garlic = Ingredient("Чеснок", 20.0, "г")
    assert str(garlic) == "Чеснок: 20.0 г"
def test1_eq():
    flour1 = Ingredient("Кукурузный крахмал", 5, "ц")
    flour2 = Ingredient("Кукурузный крахмал", 5, "ц")
    assert flour1 == flour2
def test2_eq():
    flour1 = Ingredient("чеснок", 5, "ц")
    flour2 = Ingredient("Кукурузный крахмал", 5, "ц")
    assert flour1 != flour2
def test3_eq():
    flour1 = Ingredient("Кукурузный крахмал", 5, "ц")
    flour2 = Ingredient("Кукурузный крахмал", 5, "г")
    assert flour1 != flour2

def test_init():
    flour = Ingredient("Кукурузный крахмал", 500.0, "ц")
    assert flour._name == "Кукурузный крахмал"
    assert flour._quantity == 500.0
    assert flour._unit == "ц"