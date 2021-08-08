
from project.hardware.hardware import Hardware
from project.software.software import Software
import unittest




class HardwareTests(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("Pesho", "HDD", 100, 500)

    def test_atributes_are_initialized(self):
        self.assertEqual(self.hardware.name, "Pesho")
        self.assertEqual(self.hardware.type, "HDD")
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.memory, 500)

    def test_when_is__inslalled__successfully(self):
        software = Software("App", "Light", 10, 50)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_when_is__uninslalled__successfully(self):
        software = Software("App", "Light", 10, 50)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)
        self.hardware.uninstall(software)
        self.assertEqual(len(self.hardware.software_components), 0)

    def test_install_exception(self):
        software = Software("App", "Light", 150, 550)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))
