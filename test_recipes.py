import pytest
from recipes import Ingredient, Recipe


def test_recipe_creation():
    ingredients = [
        Ingredient("flour", 500, "г"),
        Ingredient("egg", 2, "шт")
    ]
    recipe = Recipe("pizza", ingredients)
    
    assert recipe.title == "pizza"
    assert len(recipe.ingredients) == 2


def test_add_ingredient_new():
    recipe = Recipe("test receipt")
    x = Ingredient("sugar", 100, "г")
    recipe.add_ingredient(x)
    
    assert len(recipe) == 1
    assert recipe.ingredients[0].name == "sugar"


def test_add_ingredient_existing():
    recipe = Recipe("t")
    recipe.add_ingredient(Ingredient("flour", 700, "г"))
    recipe.add_ingredient(Ingredient("flour", 300, "г"))
    
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 1000.0


def test_scale():
    recipe = Recipe("pizza")
    recipe.add_ingredient(Ingredient("flour", 400, "г"))
    recipe.add_ingredient(Ingredient("cheese", 200, "г"))
    
    scaled = recipe.scale(2)
    
    assert scaled.title == "pizza"
    assert len(scaled) == 2
    assert scaled.ingredients[0].quantity == 800.0
    assert scaled.ingredients[1].quantity == 400.0


def test_scale_negative_ratio():
    recipe = Recipe("Тест")
    with pytest.raises(ValueError):
        recipe.scale(-1)


def test_len():
    recipe = Recipe("pasta")
    assert len(recipe) == 0
    
    recipe.add_ingredient(Ingredient("pasta", 300, "г"))
    assert len(recipe) == 1