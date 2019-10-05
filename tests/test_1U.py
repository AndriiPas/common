import unittest


from homework import get_rectangle_perimeter


class MyTestCase(unittest.TestCase):

    def test_get_rectangle_perimeter(self):
        wight, height = 10, 20
        expected_result = 60
        result = get_rectangle_perimeter(wight, height)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
