import unittest

from vo import lap, pilot


class PilotTests(unittest.TestCase):

    lap_fast = lap.Lap(
            hour='23:49:10.858',
            pilot_code='11',
            pilot_name='RACER',
            lap_number='1',
            lap_time='1:04.352',
            speed='43,243'
            )
    lap_slow = lap.Lap(
            hour='23:49:10.858',
            pilot_code='11',
            pilot_name='RACER',
            lap_number='1',
            lap_time='2:08.000',
            speed='22,243'
            )
    laps = [lap_fast, lap_slow]
    name = 'RACER'
    code = 11

    def test_init(self):
        p = pilot.Pilot(self.code, self.name, self.laps)
        self.assertIsNotNone(p.code, 'code variable test failed')
        self.assertIsNotNone(p.name, 'name variable test failed')
        self.assertIsNotNone(p.laps, 'laps variable test failed')

    def test_fastest_lap(self):
        p = pilot.Pilot(self.code, self.name, self.laps)
        self.assertEqual(p.fastest_lap(), self.lap_fast)

    def test_total_laps(self):
        p = pilot.Pilot(self.code, self.name, self.laps)
        self.assertEqual(p.total_laps(), len(self.laps))

    def test_total_racetime(self):
        p = pilot.Pilot(self.code, self.name, self.laps)
        self.assertEqual(p.total_racetime(), '03:12.352000')

    def test_calculate_speed(self):
        p = pilot.Pilot(self.code, self.name, self.laps)
        self.assertEqual(p.calculate_speed(), 32.743)
