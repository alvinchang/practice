import os
import unittest


class UnitTestSuiteRunner(unittest.TestCase):

    def test_all_unit_tests(self):
        loader = unittest.TestLoader()

        root_directory = os.getcwd()

        suite = loader.discover(root_directory)

        runner = unittest.TextTestRunner()
        runner.run(suite)
