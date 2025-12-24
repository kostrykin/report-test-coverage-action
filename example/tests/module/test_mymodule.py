import mymodule
import unittest


class MyModuleTest(unittest.TestCase):

    def test_divide(self):
        actual = mymodule.divide(5, 2)
        self.assertAlmostEqual(actual, 2.5)