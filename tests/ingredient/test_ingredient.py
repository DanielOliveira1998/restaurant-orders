from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    fisrt_ingredient = Ingredient("farinha")
    second_ingredient = Ingredient("farinha")
    third_ingredient = Ingredient("bacon")
    third_ingredient_restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert hash(fisrt_ingredient) == hash(second_ingredient)
    assert hash(third_ingredient) != hash(fisrt_ingredient)
    assert fisrt_ingredient.__eq__(second_ingredient)
    assert fisrt_ingredient.__eq__(fisrt_ingredient)
    assert not third_ingredient.__eq__(fisrt_ingredient)
    assert repr(fisrt_ingredient) == "Ingredient('farinha')"
    assert fisrt_ingredient.name == "farinha"
    assert third_ingredient.restrictions == third_ingredient_restrictions
