class Ingredient:
    
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.unit = unit
        self.quantity = quantity  
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)
    
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name and self.unit == other.unit
    
class Recipe:
    
    def __init__(self, title: str, ingredients=None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients
    
    def add_ingredient(self, ingredient):
        for item in self.ingredients:
            if item == ingredient:
                item.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        if ratio > 0:
            return True
        return False
    
    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Ratio должен быть положительным")
        
        ingredients_0 = []
        for x in self.ingredients:
            nx = Ingredient(x.name, x.quantity * ratio, x.unit)
            ingredients_0.append(nx)
        
        return Recipe(self.title, ingredients_0)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        result = f"Рецепт: {self.title}\nИнгредиенты:\n"
        for x in self.ingredients:
            result += f"  {x}\n"
        return result
