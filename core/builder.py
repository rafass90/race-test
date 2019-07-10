import re

from core.race_controller import RaceController
from vo import lap, pilot


class Builder:
    @staticmethod
    def build_laps(file_text):
        laps = list()
        for text_line in file_text:
            lp = Builder._read_line(text_line)
            if lp is not None:
                laps.append(lp)
        return laps

    @staticmethod
    def build_race(laps):
        pilot_names = Builder._identify_pilots(laps)
        pilots = []
        for pilot_name in pilot_names:
            pilot_laps = list(x for x in laps if x.pilot_name == pilot_name)
            pi = pilot.Pilot(
                pilot_laps[0].pilot_code,
                pilot_name,
                pilot_laps
            )
            pilots.append(pi)

        return RaceController(pilots)

    @staticmethod
    def regex_read_line(regex, line_str):
        matches = re.match(regex, line_str)
        if matches is not None:
            return matches.groups()

    @staticmethod
    def _read_line(text_line):
        line_str = Builder.regex_read_line(regex=lap.log_regex, line_str=text_line)
        return lap.lap_builder(line_str)

    @staticmethod
    def _identify_pilots(laps):
        return set(list(l.pilot_name for l in laps))
