from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    dish_instance1 = Dish("comida A", 5.00)
    dish_instance2 = Dish("comida A", 5.00)
    dish_instance3 = Dish("comida B", 7.00)
    ingredient_instace = Ingredient("tomate")
    dish_instance3.add_ingredient_dependency(ingredient_instace, 3)
    assert dish_instance1.name == "comida A"
    assert dish_instance1 == dish_instance2
    assert dish_instance1 != dish_instance3
    assert hash(dish_instance1) == hash(dish_instance2)
    assert hash(dish_instance1) != hash(dish_instance3)
    assert repr(dish_instance1) == "Dish('comida A', R$5.00)"
    with pytest.raises(ValueError):
        Dish("comida C", -5.00)
    with pytest.raises(TypeError):
        Dish("comida C", "5.00")
    assert dish_instance3.get_ingredients() == {ingredient_instace}
    assert dish_instance3.get_restrictions() == ingredient_instace.restrictions
