def ingredient_in(self, ingredients, ingredient):
    for key, value in self.ingredients.items():
        if key == ingredient:
            return True
    return False

class PizzaDelivery:
    ordered = False
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        
    
    
    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        # if self.ordered:
            # return f"Pizza {self.name} already prepared, and we can't make any changes!"     
        if ingredient_in(self, self.ingredients, ingredient) and not PizzaDelivery.ordered:
            self.ingredients[ingredient] += quantity
            self.price += price_per_ingredient*quantity
        elif not ingredient_in(self, self.ingredients, ingredient) and not PizzaDelivery.ordered:
            self.ingredients[ingredient] = quantity
            self.price += price_per_ingredient*quantity
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"  

    
    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
    
        if ingredient_in(self, self.ingredients, ingredient):
            if not quantity > self.ingredients[ingredient]:
                self.ingredients[ingredient] -= quantity
                self.price -= price_per_ingredient*quantity
            else:
                return f"Please check again the desired quantity of {ingredient}!"
        elif not ingredient_in(self, self.ingredients, ingredient):
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"


    def make_order(self):
        PizzaDelivery.ordered = True
        str_ingtedients = []
        for k, v in self.ingredients.items():
            str_ingtedients.append(f'{k}: {v}')
        return f"You've ordered pizza {self.name} prepared with {', '.join(str_ingtedients)} and the price will be {self.price}lv."
        




margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

