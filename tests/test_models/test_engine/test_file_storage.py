#!/usr/bin/python3
""" This is a test for the FileStorage class"""

import unittest
from os import remove
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
