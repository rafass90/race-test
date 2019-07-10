import unittest
from datetime import timedelta

from utils.date import RaceDate


class RaceDateTests(unittest.TestCase):
    def test_convert_to_timedelta(self):
        self.assertIsInstance(RaceDate.convert_to_timedelta('03:12.034'), timedelta)
