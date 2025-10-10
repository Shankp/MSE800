import unittest

def add(x, y):
    return x + y

def Multiplication(x, y):
    return x * y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiplication(self):
        self.assertEqual(Multiplication(2, 3), 6)
        self.assertEqual(Multiplication(-1, 1), -1)

if __name__ == '__main__':
    unittest.main()
