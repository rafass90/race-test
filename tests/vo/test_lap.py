import unittest

from vo import lap


class LapTests(unittest.TestCase):
    def test_None_lap_builder(self):
        arrayNone = None
        self.assertIsNone(lap.lap_builder(arrayNone))

    def test_lap_builder(self):
        arrayNotNone = ['23:49:10.858', '033', 'R.BARRICHELLO', '1', '1:04.352', '43,243']
        self.assertIsNotNone(lap.lap_builder(arrayNotNone))

    def test_variables(self):
        msg = '{} variable test failed'

        array = ['23:49:10.858', '033', 'R.BARRICHELLO', '1', '1:04.352', '43,243']
        lap_test = lap.lap_builder(array)
        self.assertEqual('23:49:10.858', lap_test.hour, msg=msg.format('hour'))
        self.assertEqual('033', lap_test.pilot_code, msg=msg.format('pilot_code'))
        self.assertEqual('R.BARRICHELLO', lap_test.pilot_name, msg=msg.format('pilot_name'))
        self.assertEqual('1', lap_test.lap_number, msg=msg.format('lap_number'))
        self.assertEqual('1:04.352', lap_test.lap_time, msg=msg.format('lap_time'))
        self.assertEqual('43,243', lap_test.speed, msg=msg.format('speed'))
