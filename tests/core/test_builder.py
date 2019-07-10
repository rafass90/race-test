import pathlib
import unittest

from core.builder import Builder
from core.race_controller import RaceController
from utils import file
from vo import lap


class BuilderTests(unittest.TestCase):

    _lap_fast = lap.Lap(
            hour='23:49:10.858',
            pilot_code='11',
            pilot_name='RACER',
            lap_number='1',
            lap_time='1:04.352',
            speed='43,243'
            )
    _lap_slow = lap.Lap(
            hour='23:49:10.858',
            pilot_code='11',
            pilot_name='RACER',
            lap_number='1',
            lap_time='2:08.000',
            speed='22,243'
            )
    laps = [_lap_fast, _lap_slow]
    _txt_header = "Hora                               Piloto             Nº Volta   Tempo Volta       Velocidade média da volta"
    _txt_lap_default_spacing = "23:49:08.277      038 – F.MASSA                           1		1:02.852                        44,275"
    _txt_lap_minimun_spacing = "23:49:08.277   038 – F.MASSA   1   1:02.852   44,275"

    def test_build_laps(self):
        log_file = self._load_file()
        return_build = Builder.build_laps(log_file)

        self.assertIsNotNone(return_build)
        self.assertIsInstance(return_build, list)
        self.assertIsInstance(return_build[0], lap.Lap)

    def test_laps_header_doc(self):
        return_build = Builder._read_line(self._txt_header)
        self.assertIsNone(return_build)

    def test_laps_lap_default_spacing(self):
        return_build = Builder._read_line(self._txt_lap_minimun_spacing)
        self.assertIsInstance(return_build, lap.Lap)

    def test_build_race(self):
        return_build = Builder.build_race([self._lap_fast, self._lap_slow])
        self.assertIsInstance(return_build, RaceController)

    def test_identify_pilots(self):
        list_pilots = Builder._identify_pilots(self.laps)
        self.assertIsInstance(list_pilots, set)
        self.assertEqual(len(list_pilots), 1)

    def _load_file(self):
        log_path = pathlib.Path(__file__).parent / 'data/race.log'
        return file.Reader.read_file(filename=log_path)
