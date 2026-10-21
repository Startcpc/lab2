import pytest
from pathlib import Path
from streamstats.parsers import pars_csv, pars_json
from streamstats.errors import InvalidEventError


def test_pars_csv_norm() -> None:
    """парсит нормальный CSV файл"""
    csv_file = Path("tests/norm.csv")
    events = list(pars_csv(csv_file, skip_invalid=False))
    assert events


def test_pars_jsonl_norm() -> None:
    """парсит нормальный JSONL файл"""
    jsonl_file = Path("tests/norm.jsonl")
    events = list(pars_json(jsonl_file, skip_invalid=False))
    assert events

def test_empty_csv():
    """Тест пустого CSV файла"""
    csv_file = Path("tests/empty.csv")
    events = list(pars_csv(csv_file, skip_invalid=False))
    assert not events

def test_empty_jsonl():
    """Тест пустого JSONL файла"""
    jsonl_file = Path("tests/empty.jsonl")
    events = list(pars_csv(jsonl_file, skip_invalid=False))
    assert not events

def test_pars_csv_bad_no_skip() -> None:
    """Тест повреждённой строки в CSV"""
    csv_file = Path("tests/bad.csv")
    with pytest.raises(InvalidEventError):
        list(pars_csv(csv_file, skip_invalid=False))

def test_pars_jsonl_bad_no_skip() -> None:
    """Тест поврежденной строки в JSONL"""
    jsonl_file = Path("tests/bad.jsonl")
    with pytest.raises(InvalidEventError):
        list(pars_json(jsonl_file, skip_invalid=False))
