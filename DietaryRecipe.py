from Recipe import Recipe
class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        scaled_base = super().scale(ratio)

        return DietaryRecipe(
            title=scaled_base._title,
            diet_type=self.diet_type,
            ingredients=scaled_base._ingredients
        )
    def __str__(self):
        return "[" + self.diet_type + "] " + super().__str__()