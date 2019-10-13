import unittest
from math import sqrt, pow

from homework_test import Rectangle


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.width, self.height = 6, 8
        self.rectangle = Rectangle(self.width, self.height)
        self.circle = Rectangle(self.width, self.width)

    def test_get_rectangle_perimeter(self):
        result_prog = self.rectangle.get_rectangle_perimeter()
        result_test = (self.width + self.height) * 2
        self.assertEqual(result_prog, result_test)

    def test_get_rectangle_square(self):
        result_prog = self.rectangle.get_rectangle_square()
        result_test = self.width * self.height
        self.assertEqual(result_prog, result_test)

    def test_num_cor(self):
        result_test = 0
        for i in range(1, 5):
            result_prog = Rectangle.get_sum_of_corners(self, i)
            result_test += 90
            self.assertEqual(result_prog, result_test)
        with self.assertRaises(ValueError):
            Rectangle.get_sum_of_corners(self, 5)

    def test_re_diag(self):
        result_prog = self.rectangle.get_rectangle_diagonal()
        result_test = sqrt(pow(self.width, 2) + pow(self.height, 2))
        self.assertEqual(result_prog, result_test)

    def test_rcc(self):
        result_test = (sqrt(pow(self.width, 2) + pow(self.height, 2))) / 2
        result_prog = self.rectangle.get_radius_of_circumscribed_circle()
        self.assertEqual(result_prog, result_test)

    def test_ric_error(self):
        with self.assertRaises(ValueError):
            Rectangle(self.height, self.width).get_radius_of_inscribed_circle()

    def test_ric(self):
        result_test = self.width / 2
        result_prog = self.circle.get_radius_of_inscribed_circle()
        self.assertEqual(result_prog, result_test)


if __name__ == '__main__':
    unittest.main()
