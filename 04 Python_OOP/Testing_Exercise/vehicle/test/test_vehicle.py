import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):

        self.vehicle = Vehicle(10, 50)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 10)
        self.assertEqual(self.vehicle.horse_power, 50)
        self.assertEqual(self.vehicle.capacity, 10)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive(self):
        km = 5
        self.vehicle.drive(km)
        self.assertEqual(self.vehicle.fuel, 3.75)


    def test_drive_exception(self):
        km = 10
        with self.assertRaises(Exception) as exc:
            self.vehicle.drive(km)
        self.assertEqual("Not enough fuel", str(exc.exception))
    def test_refuel(self):
        self.vehicle.fuel -= 20
        fuel = 10
        self.vehicle.refuel(fuel)
        self.assertEqual(self.vehicle.fuel, 0)
    def test_refuel_exception(self):
        fuel = 10
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(fuel)
        self.assertEqual("Too much fuel", str(exc.exception))

    def test_str_method(self):
        horse_power = self.vehicle.horse_power
        fuel = self.vehicle.fuel
        fuel_consumption = 1.25
        self.assertEqual(f"The vehicle has {horse_power} horse power with {fuel} fuel left and {fuel_consumption} fuel consumption", str(self.vehicle))



# if __name__ == "__main__":
#     unittest.main()

