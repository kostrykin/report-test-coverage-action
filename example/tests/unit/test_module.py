import module
import unittest

from .. import tools


class ModuleTest(unittest.TestCase):

    def test_divide(self):
        actual = module.divide(5, 2)
        expected = 2.5
        self.assertAlmostEqual(actual, 2.5)

    def test_divide_zero(self):
        actual = module.divide(0, 0)
        self.assertAlmostEqual(actual, 0)