#!/usr/bin/python3
""" This is a test for the FileStorage class"""

import unittest
from os import remove
import os
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """ This is a test for the FileStorage class """

    def setUp(self):
        """ Try delete the file.json file"""
        try:
            remove('file.json')
        except BaseException:
            pass

    def tearDown(self):
        """ Try delete the file.json file after each test """
        try:
            remove('file.json')
        except BaseException:
            pass

    def test_pep8(self):
        """ Test for the pep8 formating"""
        styles = pep8.StyleGuide(quiet=True)
        checks = styles.check_files(['models/engine/file_storage.py'])

        self.assertEqual(checks.total_errors, 0,
                         'pep8 fail: {}'.format(checks.total_errors))

    def test_valid_atributes(self):
        """ Validate the attributes of the FileStorage """
        all_objs = storage.all()

        self.assertTrue(type(all_objs), "<class 'dict'>")

    def test_new(self):
        """ Testing the new method """
        ins = BaseModel()
        ins.save()
        all_objs = storage.all()

        obj_key = ins.__class__.__name__ + '.' + ins.id
        self.assertEqual(all_objs[obj_key], ins)
        self.assertEqual(obj_key in all_objs, True)

    def test_A_reload_method_empty(self):
        """
        Test reload method
        """
        all_objs = storage.all()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_B_reload_method_(self):
        """ Test reload method."""
        ins = BaseModel()
        ins.save()

        storage.reload()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

    def test_file_json(self):
        """Test for check file.json """
        my_model = BaseModel()
        my_model.save()
        here = os.path.exists('file.json')
        self.assertEqual(here, True)

    def test_models_init(self):
        """ Test models/__init__.py """
        strg = FileStorage()
        self.assertIsInstance(strg, FileStorage)
