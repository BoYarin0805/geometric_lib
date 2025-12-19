import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_positive_side(self):
        self.assertEqual(area(5), 25)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_float_side(self):
        self.assertEqual(area(2.5), 6.25)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float_side(self):
        self.assertEqual(perimeter(2.5), 10)


if __name__ == "__main__":
    unittest.main()
