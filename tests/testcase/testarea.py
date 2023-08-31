import unittest
from tests import area
from math import pi


class TestAreaFunction(unittest.TestCase):
    def test_area_function(self):
        self.assertAlmostEqual(area.area_of_a_circle(1), pi)
        self.assertAlmostEqual(area.area_of_a_circle(0), 0)
        self.assertAlmostEqual(area.area_of_a_circle(2), pi * 2 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, area.area_of_a_circle, -1)
        self.assertRaises(ValueError, area.area_of_a_circle, -5)

    def test_radius_type(self):
        self.assertRaises(TypeError, area.area_of_a_circle, True)
        self.assertRaises(TypeError, area.area_of_a_circle, 2 + 5j)
