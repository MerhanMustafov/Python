from Test_Worker import Worker

import unittest
class WorkerTests(unittest.TestCase):
    name = "pesho"
    salary = 1000
    energy = 3
    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)
    def test_correct_initialization_of_name_salary_and_energy(self):
        """•	Test if the worker is initialized with correct name, salary and energy
            """
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)
    def test_when_rest_method_is_called__is_energy_incremented(self):
        """ •	Test if the worker's energy is incremented after the rest method is called"""
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_when_energy_is_0_expected_exception(self):
        """•	Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()
    def test_when_energy_is_above_0_expected_money_to_be_increased(self):
        """    •	Test if the worker's money is increased by his salary correctly after the work method is called"""
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)


    def test_when_energy_is_above_0_expected_money_to_be_decremented(self):
        """•	Test if the worker's energy is decreased after the work method is called"""
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)
    def test_worker_get_info_expect_correct_value(self):
        """•	Test if the get_info method returns the proper string with correct values
        """
        expected = f'{self.name} has saved 0 money.'
        actual = self.worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

