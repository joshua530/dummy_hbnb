import unittest
from models.review import Review
import pycodestyle


class ReviewTest(unittest.TestCase):
    def test_pycodestyle_conformity(self):
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(["models/review.py"])
        self.assertEqual(0, res.total_errors)

    def test_contains_required_attributes(self):
        o = Review()
        self.assertTrue(hasattr(o, "place_id"))
        self.assertTrue(hasattr(o, "user_id"))
        self.assertTrue(hasattr(o, "text"))
