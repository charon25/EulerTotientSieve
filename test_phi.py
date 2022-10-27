import unittest

from benchmark import naive_method, prime_factors_method
from phi import compute_phi


class TestPhi(unittest.TestCase):

    def test_base_case(self):
        self.assertListEqual(compute_phi(3), [0, 1, 1])

    def test_limit_50(self):
        CORRECT_VALUES = [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42]

        self.assertListEqual(compute_phi(50), CORRECT_VALUES)

    def test_limit_100000(self):
        with open('test_phi_100000.txt', 'r') as fi:
            CORRECT_VALUES = list(map(int, fi.read().splitlines()))

        self.assertListEqual(compute_phi(100000), CORRECT_VALUES)

    def test_naive_method(self):
        CORRECT_VALUES = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42]

        self.assertListEqual(naive_method(50), CORRECT_VALUES)

    def test_product_prime_method(self):
        CORRECT_VALUES = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42]

        self.assertListEqual(prime_factors_method(50), CORRECT_VALUES)


if __name__ == '__main__':
    unittest.main()
