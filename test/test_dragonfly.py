
import unittest
import numpy as np

from algo import EnvSetup
from dragonfly import Dragonfly
from numpy.testing import assert_array_equal

class Test(unittest.TestCase):

    def setUp(self):
        self.setting = EnvSetup(1, 2, 3, 4, 5, 6)

    def test_dragonfly_dist(self):
        self.d1 = Dragonfly(0, np.zeros(3), self.setting)
        self.d2 = Dragonfly(1, np.zeros(3), self.setting)
        self.assertEqual(self.d1.dist(self.d2), 0.0)

    def test_dragonfly_dist_2(self):
        self.d1 = Dragonfly(0, np.array([1, 2, 3]), self.setting)
        self.d2 = Dragonfly(1, np.zeros(3), self.setting)
        self.assertAlmostEqual(self.d1.dist(self.d2), 3.741, 2)




