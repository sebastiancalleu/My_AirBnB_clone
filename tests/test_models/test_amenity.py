#!/usr/bin/python3
""" This is a test for the base_model class"""

import pep8
import unittest
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """
    AmenityTest
    class that tests
    city Amenity
    """

    def test_Pep8(self):
        """
        test_pep8
        test for pep8
        """
        pep8val = pep8.StyleGuide(quiet=True)
        pep8checks = pep8val.check_files(["models/amenity.py"])
        self.assertEqual(pep8checks.total_errors, 0, "pep8 fail")

    def test_instance(self):
        """
        test_instance
        class that test
        for class Amenity
        """
        ins = Amenity()
        self.assertIsInstance(ins, Amenity)
