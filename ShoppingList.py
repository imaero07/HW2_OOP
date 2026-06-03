from Ingredient import Ingredient
from Recipe import Recipe
class ShoppingList:
    def __init__(self):
        self._items=[]
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for i in scaled._ingredients:
            self._items.append((i, scaled._title))

    def remove_recipe(self, title: str):
        for ingredient, recipeTitle in self._items[:]:
            if recipeTitle == title:
                self._items.remove((ingredient, recipeTitle))

    def get_list(self) -> dict:
        final_list = {}
        for ingredient, recipeTitle in self._items[:]:
            key = (ingredient._name, ingredient._unit)
            if key in final_list:
                final_list[key]['quantity'] += ingredient.quantity
            else:
                final_list[key] = {
                    'quantity': ingredient.quantity
                }
        result = []
        for (name, unit), data in final_list.items():
            result.append(Ingredient(name, data['quantity'], unit))
        result.sort(key=lambda x: x._name)

        return result
    def __add__(self, other: 'ShoppingList'):
        fullList = ShoppingList()
        fullList._items.extend(self._items)
        fullList._items.extend(other._items)
        return fullList





