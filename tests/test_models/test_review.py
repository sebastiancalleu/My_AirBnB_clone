#!/usr/bin/python3
""" This is a test for the base_model class"""

import pep8
import unittest
from models.review import Review


class reviewTest(unittest.TestCase):
    """
    reviewTest
    class that tests
    review class
    """

    def test_Pep8(self):
        """
        test_pep8
        test for pep8
        """
        pep8val = pep8.StyleGuide(quiet=True)
        pep8checks = pep8val.check_files(["models/review.py"])
        self.assertEqual(pep8checks.total_errors, 0, "pep8 fail")

    def test_instance(self):
        """
        test_instance
        class that test
        for class review
        """
        ins = Review()
        self.assertIsInstance(ins, Review)
