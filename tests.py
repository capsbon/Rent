import unittest
import small.double_nine
from small import double_nine, duplicated_list


class TestTrans(unittest.TestCase):

    def test_double_nine_left(self):
        result = '1\n2  4\n3  6  9\n4  8 12 16\n5 10 15 20 25\n6 12 18 24 30 36\n7 14 21 28 35 42 49\n8 16 24 32 40 48 56 64\n9 18 27 36 45 54 63 72 81\n'
        self.assertEqual(double_nine(right=False), result)

    def test_double_nine_right(self):
        result = '1  2  3  4  5  6  7  8  9\n   4  6  8 10 12 14 16 18\n      9 12 15 18 21 24 27\n        16 20 24 28 32 36\n           25 30 35 40 45\n              36 42 48 54\n                 49 56 63\n                    64 72\n                       81\n'
        self.assertEqual(double_nine(right=True), result)

    # def test_duplicated_list(self):
    #     self.assertEqual(
    #         duplicated_list([1, 2, 3, 2, 1, 10, 5, 5, 1]),
    #         [1, 2, 2, 1, 5, 5, 1]
    #     )


if __name__ == '__main__':
    double_nine()
    #unittest.main()
