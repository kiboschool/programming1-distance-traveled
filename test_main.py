import unittest
from main import *

class DistanceTraveled(unittest.TestCase):
    def test_distance_function_defined(self):
        distance((0.0, 0.0), (0.0, 0.0))

    def test_distance(self):
        self.assertEquals(distance((1.0, 0.0), (2.0,0.0)), 1)
        self.assertEquals(distance((0.0, 1.0), (0.0,2.0)), 1)
        self.assertEquals(distance((0.0, 0.0), (3.0,4.0)), 5)

    def test_total_distance(self):
        empty_travel = []
        zeroes_travel = [(0.0, 0.0), (0.0, 0.0)]
        travel_345 = [(0.0, 0.0),(3.0, 4.0)]
        self.assertEquals(total_distance(empty_travel), 0.0)
        self.assertEquals(total_distance(zeroes_travel),0.0)
        self.assertEquals(total_distance(travel_345),5.0)
        short_travel = [
              (1.0, 3.0),
              (1.2, 3.2),
              (1.4, 3.2),
              (1.6, 2.8),
              (1.8, 3.0),
              (2.2, 3.0)
              ]
        self.assertAlmostEquals(total_distance(short_travel),1.6129, 4)

if __name__ == '__main__':
    unittest.main()
