import unittest

from core.race_controller import RaceController
from vo import lap, pilot


class RaceTests(unittest.TestCase):

    min_laps = 4
    best_lap = None
    winner = None
    race_result = None

    def test_init(self):
        pilot_slow = self.create_slow_mock()
        pilot_fast = self.create_fast_mock()
        r = RaceController([pilot_slow, pilot_fast])
        self.assertIsNotNone(r.pilots)

    def test_get_best_lap(self):
        pilot_slow = self.create_slow_mock()
        pilot_fast = self.create_fast_mock()
        r = RaceController([pilot_slow, pilot_fast])
        r.calculate_race_result()
        self.assertEqual(r.best_lap.lap_time, '1:04.352')

    def test_get_winner_with_no_finished_race(self):
        pilot_slow = self.create_slow_mock()
        pilot_fast = self.create_fast_mock()
        r = RaceController([pilot_slow, pilot_fast])
        r.calculate_race_result()
        self.assertIsNone(r.winner)

    def test_get_winner_with_finished_race(self):
        pilot_slow = self.create_slow_mock()
        pilot_fast = self.create_fast_mock()
        pilot_winner = self.create_winner_mock()
        r = RaceController([pilot_slow, pilot_fast, pilot_winner])
        r.calculate_race_result()
        self.assertIsNotNone(r.winner)

    def test_calculate_race_result(self):
        pilot_slow = self.create_slow_mock()
        pilot_fast = self.create_fast_mock()
        r = RaceController([pilot_slow, pilot_fast])
        r.calculate_race_result()
        self.assertIsInstance(r.race_result, list)

    def create_winner_mock(self):
        name = 'RACERWINNER'
        code = '06'
        lap1 = lap.Lap(
                    hour='23:49:10.858',
                    pilot_code=code,
                    pilot_name=name,
                    lap_number='1',
                    lap_time='1:04.352',
                    speed='43,243'
                    )
        lap2 = lap.Lap(
                hour='23:49:10.858',
                pilot_code=code,
                pilot_name=name,
                lap_number='2',
                lap_time='2:08.000',
                speed='22,243'
                )
        lap3 = lap.Lap(
                hour='23:49:10.858',
                pilot_code=code,
                pilot_name=name,
                lap_number='3',
                lap_time='2:08.000',
                speed='22,243'
                )
        lap4 = lap.Lap(
                hour='23:49:10.858',
                pilot_code=code,
                pilot_name=name,
                lap_number='4',
                lap_time='2:08.000',
                speed='22,243'
                )
        laps = [lap1, lap2, lap3, lap4]
        return self.create_mock(code, name, laps)

    def create_fast_mock(self):
        name = 'RACERFAST'
        code = '10'
        slow_lap_fast = lap.Lap(
                    hour='23:49:10.858',
                    pilot_code=code,
                    pilot_name=name,
                    lap_number='1',
                    lap_time='1:04.352',
                    speed='43,243'
                    )

        slow_lap = lap.Lap(
                hour='23:49:10.858',
                pilot_code=code,
                pilot_name=name,
                lap_number='2',
                lap_time='2:08.000',
                speed='22,243'
                )
        laps = [slow_lap_fast, slow_lap]
        return self.create_mock(code, name, laps)

    def create_slow_mock(self):
        name = 'RACERSLOW'
        code = '11'
        slow_lap_fast = lap.Lap(
                    hour='23:49:10.858',
                    pilot_code=code,
                    pilot_name=name,
                    lap_number='1',
                    lap_time='2:04.352',
                    speed='23,243'
                    )

        slow_lap = lap.Lap(
                hour='23:49:10.858',
                pilot_code=code,
                pilot_name=name,
                lap_number='2',
                lap_time='3:08.000',
                speed='12,243'
                )
        laps = [slow_lap_fast, slow_lap]
        return self.create_mock(code, name, laps)

    def create_mock(self, code, name, laps):
        return pilot.Pilot(code, name, laps)
