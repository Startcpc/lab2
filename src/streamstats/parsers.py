from collections.abc import Generator
from csv import DictReader
from csv import Error as CSVDecodeError
from json import JSONDecodeError, loads
from pathlib import Path
from pydantic import ValidationError
from .exceptions import validation
from .models import Event


def pars_csv(
    file_path: Path, skip_invalid: bool = False
) -> Generator[Event, None, int]:
  skipped_lines = 0
  with file_path.open(mode='r', encoding='utf-8', newline='') as file:
    rad = DictReader(file)
    line_num = 2
    for i in rad:
      try:
        event = Event.model_validate(i)
        yield event
      except (ValidationError, CSVDecodeError) as error:
        res = validation(error, file_path.name, line_num, skip_invalid)
        if res is None:
          skipped_lines += 1
          line_num += 1
          continue
        raise res
      line_num += 1
  return skipped_lines


def pars_json(
    file_path: Path, skip_invalid: bool = False
) -> Generator[Event, None, int]:
  skipped_lines = 0
  with file_path.open(mode='r', encoding='utf-8', newline='') as file:
    line_num = 1
    for i in file:
      try:
        data = loads(i)
        event = Event.model_validate(data)
        yield event
      except (ValidationError, JSONDecodeError) as error:
        res = validation(error, file_path.name, line_num, skip_invalid)
        if res is None:
          skipped_lines += 1
          line_num += 1
          continue
        raise res
      line_num += 1
  return skipped_lines
