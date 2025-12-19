import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_with_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_rectangle(self):
        self.assertEqual(area(5, 7), 35)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter(3, 7), 20)

    def test_perimeter_with_zero(self):
        self.assertEqual(perimeter(5, 0), 10)


if __name__ == "__main__":
    unittest.main()
