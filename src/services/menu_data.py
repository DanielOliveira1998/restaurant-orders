import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(file=source_path, mode="r") as file:
            csv_data = csv.DictReader(file)
            self.dishes = set()
            dishes_dict = {}
            for row in csv_data:
                if not row["dish"] in dishes_dict:
                    dish = Dish(row["dish"], float(row["price"]))
                    ingredient = Ingredient(row["ingredient"])
                    recipe_amount = int(row["recipe_amount"])
                    dish.add_ingredient_dependency(ingredient, recipe_amount)
                    dishes_dict[row["dish"]] = dish
                else:
                    ingredient = Ingredient(row["ingredient"])
                    recipe_amount = int(row["recipe_amount"])
                    dishes_dict[row["dish"]].add_ingredient_dependency(
                        ingredient, recipe_amount
                    )
            self.dishes.update(dishes_dict.values())
