import unittest
from models.place import Place
import pycodestyle


class PlaceTest(unittest.TestCase):
    def test_pycodestyle_conformity(self):
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(["models/place.py"])
        self.assertEqual(0, res.total_errors)

    def test_contains_required_attributes(self):
        o = Place()
        self.assertTrue(hasattr(o, "city_id"))
        self.assertTrue(hasattr(o, "user_id"))
        self.assertTrue(hasattr(o, "name"))
        self.assertTrue(hasattr(o, "description"))
        self.assertTrue(hasattr(o, "number_rooms"))
        self.assertTrue(hasattr(o, "number_bathrooms"))
        self.assertTrue(hasattr(o, "max_guest"))
        self.assertTrue(hasattr(o, "price_by_night"))
        self.assertTrue(hasattr(o, "latitude"))
        self.assertTrue(hasattr(o, "longitude"))
        self.assertTrue(hasattr(o, "amenity_ids"))
        self.assertIsInstance(o.amenity_ids, list)
