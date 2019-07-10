import pathlib
import sys

from core.builder import Builder
from utils.file import Reader, Writer


def gympass_race(params):
    if len(params) >= 3:
        log_path = str(params[1])
        result_race_path = str(params[2])
    else:
        log_path = pathlib.Path(__file__).parent / 'data/race.log'
        result_race_path = pathlib.Path(__file__).parent / 'data/result.txt'

    race_log = Reader.read_file(filename=log_path)

    laps = Builder.build_laps(race_log)
    gympass_race = Builder.build_race(laps)

    gympass_race.calculate_race_result()

    Writer.write_file(filename=result_race_path,
                      content=gympass_race.asdict()
                      )


if __name__ == '__main__':
    gympass_race(sys.argv)
