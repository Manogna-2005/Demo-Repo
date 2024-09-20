def subtract(a,b):
    return (a-b)

import unittest
class subtractclass(unittest.TestCase):
    def test1(self):
        result = subtract(10,7)
        self.assertEqual(result, 3)
    def test2(self):
        result = subtract(-10,-7)
        self.assertEqual(result, -3)
    def test3(self):
        result = subtract(10,-7)
        self.assertEqual(result, 17)
    def test4(self):
        result = subtract(10,0)
        self.assertEqual(result, 10)
    def test5(self):
        result = subtract(-10,0)
        self.assertEqual(result, -10)
        



if __name__ == '__main__':
    unittest.main()
