import unittest

from Functions import *


class MyTestCase(unittest.TestCase):

    def test_task_1(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 3, 4, 5, 6]
        res_list = [2, 3, 4, 5]
        lst = task_1(a, b)
        self.assertEqual(lst, res_list)

    def test_task_2(self):
        self.assertEqual(task_2('I am a good developer'), 2)

    def test_task_3_true(self):
        self.assertTrue(task_3(9))
        self.assertTrue(task_3(27))

    def test_task_3_falce(self):
        self.assertFalse(task_3(5))

    def test_task_4(self):
        self.assertEqual(task_4(34), 7)

    def test_task_5(self):
        self.assertEqual(task_5([0, 2, 0, 3, 5, 6, 7, 10]), [2, 3, 5, 6, 7, 10, 0, 0])

    def test_task_7(self):
        self.assertEqual(task_7([5, 3, 4, 3, 4, 8]), [5, 8])

    def test_task_8(self):
        self.assertEqual(task_8([1, 2, 3, 4, 7, 8]), [5, 6])

    def test_task_9(self):
        self.assertEqual(task_9([1, 2, 3, (1, 2), 3]), 3)

    def test_task_10(self):
        self.assertEqual(task_10(("Hello World and Coders")), "sredoC dna dlroW olleH")

    def test_task_11(self):
        self.assertEqual(task_11(63), "1:3")

    def test_task_12(self):
        self.assertEqual(task_12("fun&!! time"), "time")

    def test_task_13(self):
        self.assertEqual(task_13("My name is Michele"), "Michele is name My")

    def test_task_14(self):
        self.assertEqual(task_14(6), [1, 1, 2, 3, 5, 8])

    def test_task_15(self):
        self.assertEqual(task_15([1, 1, 2, 3, 5, 8]), [2, 8])

    def test_task_16(self):
        self.assertEqual(task_16(4), 10)

    def test_task_17(self):
        self.assertEqual(task_17(4), 24)

    def test_task_18(self):
        self.assertEqual(task_18('abcd'), 'bcde')

    def test_task_19(self):
        self.assertEqual(task_19('edcba'), 'abcde')

    def test_task_20(self):
        self.assertEqual(task_20(4, 5), True)
        self.assertEqual(task_20(5, 4), False)


if __name__ == '__main__':
    unittest.main()
