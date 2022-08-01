import unittest
import pycodestyle


class ConsoleTest(unittest.TestCase):
    def test_pycodestyle_compliance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(["console.py"])
        self.assertEqual(res.total_errors, 0)
