import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pycodestyle
import os
from models import storage

class FileStorageTest(unittest.TestCase):
    __file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file.json")

    def setUp(self):
        # delete any stored objects to start on a new slate
        try:
            os.remove(FileStorageTest.__file)
            storage.reload()
        except FileNotFoundError:
            pass

    def test_pycodestyle_conformity(self):
        style = pycodestyle.StyleGuide(quiet=True)
        res = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(res.total_errors, 0)

    def test_stored_objs_are_dict(self):
        o = FileStorage()
        self.assertIsInstance(o.all(), dict)

    def test_new_object_is_stored(self):
        o = BaseModel()
        o.foo = 'bar'
        storage.new(o)
        key = "{}.{}".format(o.__class__.__name__, o.id)
        stored_items = storage.all()
        self.assertTrue(key in stored_items.keys())

    def test_objects_saved_to_file(self):
        '''save and retrieve objects to ensure they were saved correctly
        
        tests new, save and reload
        '''
        o = BaseModel()
        o2 = BaseModel()
        o_id = '{}.{}'.format(o.__class__.__name__, o.id)
        o2_id = '{}.{}'.format(o2.__class__.__name__, o2.id)
        storage.new(o)
        storage.new(o2)
        storage.save()
        storage.reload()
        stored_items = storage.all()
        self.assertTrue(o_id in stored_items.keys())
        self.assertTrue(o2_id in stored_items.keys())
