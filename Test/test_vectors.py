import unittest
import env
from terminalapp.vectors import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point()
        self.p2 = Point(1, 1)
        self.p3 = Point(5, 5)

    def test_add(self):
        self.p1 += self.p2
        self.assertEqual(str(self.p1), "(1, 1)")

    def test_sub(self):
        self.p2 -= self.p3
        self.assertEqual(str(self.p2), "(-4, -4)")

    def test_mul(self):
        self.p2 *= self.p3
        self.assertEqual(str(self.p2), "(5, 5)")


if __name__ == "__main__":
    unittest.main()
