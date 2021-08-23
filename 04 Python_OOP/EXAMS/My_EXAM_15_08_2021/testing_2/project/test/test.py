import unittest

from project.pet_shop import PetShop

class PetShopTests(unittest.TestCase):
    def setUp(self):
        self.pet_shop = PetShop("Name")

    def test_init(self):
        self.assertEqual(self.pet_shop.name, "Name")
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])

    def test_add_food_quantity_under_0(self):
        name = "Name"
        quantity = -1
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food(name, quantity)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_name_not_in_food(self):
        name = "Name"
        quantity = 1
        actual = self.pet_shop.add_food(name, quantity)
        self.assertEqual(actual, f"Successfully added {quantity:.2f} grams of {name}.")
        self.assertEqual(self.pet_shop.food[name], 1)


    def test_add_pet_exception(self):
        self.pet_shop.pets.append("Name")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Name")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
    def test_add_pet(self):
        actual = self.pet_shop.add_pet("Name")
        self.assertEqual(actual, f"Successfully added Name.")
        self.assertEqual(self.pet_shop.pets[0], "Name")

    def test_feed_pet_excetption(self):
        pet_name = "Name"
        food_name = "Food"
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_food_name_not_in_foods(self):
        self.pet_shop.pets.append("Name")
        pet_name = "Name"
        food_name = "Food"
        actual = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(actual, f'You do not have {food_name}')

    def test_food_under_100(self):
        self.pet_shop.pets.append("Name")
        self.pet_shop.food = {"Food": 0}
        pet_name = "Name"
        food_name = "Food"
        actual = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(actual, "Adding food...")
        self.assertEqual(self.pet_shop.food[food_name], 1000.0)

    def test_food_redusing(self):
        self.pet_shop.pets.append("Name")
        self.pet_shop.food = {"Food": 101}
        pet_name = "Name"
        food_name = "Food"
        actual = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(actual, f"{pet_name} was successfully fed")
        self.assertEqual(self.pet_shop.food[food_name], 1)

    def test_repr(self):
        self.pet_shop.pets = ["Name"]
        self.assertEqual(self.pet_shop.__repr__(), f'Shop {self.pet_shop.name}:\n'
                                                   f'Pets: {", ".join(self.pet_shop.pets)}')