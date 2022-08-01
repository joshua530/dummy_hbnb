import unittest
from models.user import User
import pycodestyle


class UserTest(unittest.TestCase):
    def test_pycodestyle_conformity(self):
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(["models/user.py"])
        self.assertEqual(0, res.total_errors)

    def test_contains_required_attributes(self):
        o = User()
        self.assertTrue(hasattr(o,"email"))
        self.assertTrue(hasattr(o,"password"))
        self.assertTrue(hasattr(o,"first_name"))
        self.assertTrue(hasattr(o,"last_name"))
