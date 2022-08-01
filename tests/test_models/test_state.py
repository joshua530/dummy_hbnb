import unittest
from models.state import State
import pycodestyle


class StateTest(unittest.TestCase):
    def test_pycodestyle_conformity(self):
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(["models/state.py"])
        self.assertEqual(0, res.total_errors)

    def test_contains_required_attributes(self):
        o = State()
        self.assertTrue(hasattr(o, "name"))
