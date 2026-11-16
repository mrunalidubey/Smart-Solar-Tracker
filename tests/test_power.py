
import unittest

from backend.algorithms.power_calculator import PowerCalculator


class TestPower(unittest.TestCase):

    def setUp(self):
        self.calculator = PowerCalculator()

    def test_power_calculation(self):
        result = self.calculator.calculate_power(1000)

        self.assertEqual(result["power"], 320)
        self.assertEqual(result["voltage"], 18)

    def test_zero_sunlight(self):
        result = self.calculator.calculate_power(0)

        self.assertEqual(result["power"], 0)
        self.assertEqual(result["current"], 0)

    def test_energy_calculation(self):
        energy = self.calculator.calculate_energy(100, 2)

        self.assertEqual(energy, 200)


if __name__ == "__main__":
    unittest.main()
