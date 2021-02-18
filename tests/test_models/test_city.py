#!/usr/bin/python3
""" This is a test for the base_model class"""

import pep8
import unittest
from models.city import City


class CityTest(unittest.TestCase):
    """
    CityTest
    class that tests
    city class
    """

    def test_Pep8(self):
        """
        test_pep8
        test for pep8
        """
        pep8val = pep8.StyleGuide(quiet=True)
        pep8checks = pep8val.check_files(["models/city.py"])
        self.assertEqual(pep8checks.total_errors, 0, "pep8 fail")

    def test_instance(self):
        """
        test_instance
        class that test
        for class city
        """
        ins = City()
        self.assertIsInstance(ins, City)
