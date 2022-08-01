import unittest
from models.city import City
import pycodestyle


class CityTest(unittest.TestCase):
    def test_pycodestyle_conformity(self):
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(["models/city.py"])
        self.assertEqual(0, res.total_errors)

    def test_contains_required_attributes(self):
        o = City()
        self.assertTrue(hasattr(o, "state_id"))
        self.assertTrue(hasattr(o, "name"))
