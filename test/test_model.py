# -*- coding: utf-8 -*-
# 
# 
import unittest

from src.models import Coordinates


class CoordinatesTest(unittest.TestCase):

    def setUp(self):
        self.coordinates = Coordinates(2, '10')

    def test_model(self):

        self.assertTrue(hasattr(self.coordinates.__attrs_attrs__, 'x'))
        self.assertTrue(self.coordinates.__attrs_attrs__.x.converter is int)
        self.assertTrue(self.coordinates.__attrs_attrs__.x.type is int)
        self.assertIsNotNone(self.coordinates.__attrs_attrs__.x.validator)

        self.assertTrue(hasattr(self.coordinates.__attrs_attrs__, 'y'))
        self.assertTrue(self.coordinates.__attrs_attrs__.y.converter is int)
        self.assertTrue(self.coordinates.__attrs_attrs__.y.type is int)
        self.assertIsNotNone(self.coordinates.__attrs_attrs__.y.validator)

    def test_validate_x_value_ok(self):
        self.coordinates.__attrs_attrs__.x.validator(
            self.coordinates,
            self.coordinates.__attrs_attrs__.x,
            10)

    def test_validate_x_value_invalid(self):
        self.\
            assertRaises(ValueError,
                         self.coordinates.__attrs_attrs__.x.validator,
                         self.coordinates,
                         self.coordinates.__attrs_attrs__.x,
                         -10)

    def test_validate_x_value_invalid_message(self):
        with self.assertRaises(ValueError) as error:
            self.coordinates.__attrs_attrs__.x.validator(
                self.coordinates,
                self.coordinates.__attrs_attrs__.x,
                -10)
        self.assertEqual(error.exception.__str__(),
                         f"{self.coordinates.__attrs_attrs__.x.name}" \
                         " must be positive")

    def test_validate_y_value_ok(self):
        self.coordinates.__attrs_attrs__.y.validator(
            self.coordinates,
            self.coordinates.__attrs_attrs__.y,
            10)

    def test_validate_x_value_invalid(self):
        self.\
            assertRaises(ValueError,
                         self.coordinates.__attrs_attrs__.y.validator,
                         self.coordinates,
                         self.coordinates.__attrs_attrs__.y,
                         2)

    def test_validate_x_value_invalid_message(self):
        with self.assertRaises(ValueError) as error:
            self.coordinates.__attrs_attrs__.y.validator(
                self.coordinates,
                self.coordinates.__attrs_attrs__.y,
                2)
        self.assertEqual(error.exception.__str__(),
                         f"{self.coordinates.__attrs_attrs__.y.name}" \
                         " must be positive")
