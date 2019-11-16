import unittest

from homework import Cat


class MyTestCase(unittest.TestCase):
    #def test_set_average_speed(self):
     #   self.assertEqual(Cat(1), )
    def test_saturation_level_value(self):
        self.assertEqual(Cat.saturation_level, 50)

    def test_increase_saturation_level(self):
        my_cat = Cat(1)
        my_cat._increase_saturation_level(10)
        self.assertEqual(my_cat.saturation_level, 60)

    def test_increase_saturation_level_max(self):
        my_cat = Cat(1)
        my_cat._increase_saturation_level(80)
        self.assertEqual(my_cat.saturation_level, 100)

    def test_reduce_saturation_level(self):
        my_cat = Cat(2)
        my_cat._reduce_saturation_level(10)
        self.assertEqual(my_cat.saturation_level, 40)

    def test_reduce_saturation_level_min(self):
        my_cat = Cat(2)
        my_cat._reduce_saturation_level(80)
        self.assertEqual(my_cat.saturation_level, 0)


if __name__ == '__main__':
    unittest.main()
