import unittest
from models.base_model import BaseModel
from datetime import datetime
import pycodestyle

class BaseModelTest(unittest.TestCase):
    def test_str_representation(self):
        o = BaseModel()
        o.foo = 'bar'
        d = o.__dict__
        id = d['id']
        expect = '[{}] ({}) <{}>'\
                .format(o.__class__.__name__, id, d)
        self.assertEqual(expect, str(o))

    def test_to_dict(self):
        o = BaseModel()
        o.foo = 'bar'
        d = {
            'foo':'bar',
            'created_at': o.created_at.isoformat(), 'id': o.id, '__class__': o.__class__.__name__}
        self.assertEqual(d, o.to_dict())

    def test_instantiation_without_kwargs(self):
        o = BaseModel()
        self.assertIsInstance(o.created_at, datetime)
        self.assertIsInstance(o.id, str)

    def test_instantiation_with_kwargs(self):
        dummy_date = datetime.now()
        date_str = dummy_date.isoformat()
        d = {'foo':'bar','created_at': date_str, 'id': 'abcde', 'updated_at': date_str}
        o = BaseModel(**d)
        self.assertEqual(o.foo, d['foo'])
        self.assertEqual(o.created_at, dummy_date)
        self.assertEqual(o.updated_at, dummy_date)
        self.assertEqual(o.id, d['id'])

    def test_pycodestyle_conformity(self):
        style= pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0)
