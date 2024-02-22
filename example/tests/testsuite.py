import module
import unittest


class ModuleTest(unittest.TestCase):

    def test_divide(self):
        actual = module.divide(5, 2)
        expected = 2.5
        self.assertAlmostEqual(actual, expected)