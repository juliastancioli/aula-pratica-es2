import unittest
from utils import soma


class TestFunctions(unittest.TestCase):

    def test_somar(self):
        resultado = soma(2, 3)
        self.assertEqual(resultado, 5)


if __name__ == '__main__':
    unittest.main()
