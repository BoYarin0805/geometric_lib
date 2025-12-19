import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertEqual(area(5), math.pi * 25)

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_float_radius(self):
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)

    def test_perimeter_positive_radius(self):
        self.assertEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)


if __name__ == "__main__":
    unittest.main()
