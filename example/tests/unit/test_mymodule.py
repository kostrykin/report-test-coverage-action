import mymodule
import unittest

from .. import tools


class MyModuleTest(unittest.TestCase):

    def test_divide(self):
        actual = mymodule.divide(5, 2)
        self.assertAlmostEqual(actual, 2.5)

    def test_divide_zero(self):
        actual = mymodule.divide(0, 0)
        self.assertAlmostEqual(actual, 0)