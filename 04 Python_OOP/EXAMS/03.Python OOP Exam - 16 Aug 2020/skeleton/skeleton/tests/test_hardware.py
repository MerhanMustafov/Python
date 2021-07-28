from project.hardware.hardware import Hardware
from project.software.software import Software

import unittest

class HardwareTests(unittest.TestCase):

    def setUp(self):
        self.hardware = Hardware("G5", "heavy", 1000, 1000)

    def test_atributes_are_initialized(self):
        self.assertEqual("G5", self.hardware.name)
        self.assertEqual("heavy", self.hardware.type)
        self.assertEqual(1000, self.hardware.capacity)
        self.assertEqual(1000, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_softwere_install(self):
        softwere = Software("G6", "Light", 1000, 1000)
        self.hardware.install(softwere)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_softwere_install_raise_exception(self):
        softwere = Software("G6", "Light", 1001, 1001)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(softwere)
        self.assertEqual("Software cannot be installed", str(exc.exception))

    def test_uninstall(self):
        softwere = Software("G6", "Light", 1000, 1000)
        self.hardware.install(softwere)
        self.hardware.uninstall(softwere)
        self.assertFalse(self.hardware.software_components)




if __name__ == "__main__":
    unittest.main()