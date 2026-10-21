import logging
from csv import DictReader, Error as CSVDecodeError
from json import loads, JSONDecodeError
from pathlib import Path
from .models import Event
from pydantic import ValidationError
from .exceptions import validation

logger = logging.getLogger("streamstats")


def pars_csv(file_path: Path, skip_invalid: bool = False) -> tuple[list[Event], int]:
    events = []
    skipped_lines = 0
    with file_path.open(mode="r", encoding="utf-8", newline="") as file:
        rad = DictReader(file)
        line_num = 2
        for i in rad:
            try:
                event = Event(**i)
                events.append(event)
            except (ValidationError, CSVDecodeError) as error:
                res = validation(error, file_path.name, line_num, skip_invalid)
                if res is None:
                    skipped_lines += 1
                    line_num += 1
                    continue
                raise res
            line_num += 1
    return events, skipped_lines


def pars_json(file_path: Path, skip_invalid: bool = False) -> tuple[list[Event], int]:
    events = []
    skipped_lines = 0
    with file_path.open(mode="r", encoding="utf-8", newline="") as file:
        line_num = 1
        for i in file:
            try:
                data = loads(i)
                event = Event(**data)
                events.append(event)
            except (ValidationError, JSONDecodeError) as error:
                res = validation(error, file_path.name, line_num, skip_invalid)
                if res is None:
                    skipped_lines += 1
                    line_num += 1
                    continue
                raise res
            line_num += 1
    return events, skipped_lines
