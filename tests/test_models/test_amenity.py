import unittest
import pycodestyle
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_pycodestyle_conformity(self):
        style = pycodestyle.StyleGuide(quiet=True)
        results = style.check_files(["models/amenity.py"])
        self.assertEqual(results.total_errors, 0)

    def test_has_class_attributes(self):
        o = Amenity()
        self.assertTrue(hasattr(o, 'name'))
