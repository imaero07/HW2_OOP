
from Ingredient import Ingredient
class Recipe:
    def __init__(self, title, ingredients):
        self._title = title
        self._ingredients = list(ingredients)

    def add_ingredient(self, ingredient: Ingredient):
        if ingredient in self._ingredients:
            for i in self._ingredients:
                if i == ingredient:
                    i.quantity += ingredient.quantity
                    break
        else:
            self._ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float))  and ratio>0:
            return True
        else: return False
    def scale(self, ratio: float):
        newIngredients=[]

        for i in self._ingredients:
            newIngredient = Ingredient(i._name, i.quantity * ratio, i._unit)
            newIngredients.append(newIngredient)
        return Recipe(self._title, newIngredients)

    def __len__(self):
        unique = {(i._name, i._unit) for i in self._ingredients}
        return len(unique)
    def __str__(self):
        result = self._title + ":\n"
        for i in self._ingredients:
            result += str(i) + "\n"
        return result
