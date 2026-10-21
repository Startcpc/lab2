from json import dump
from pathlib import Path


def save(statistica: dict, output: Path) -> None:
    """Записываем в json файлик"""
    with Path(output).open("w", encoding="utf-8") as file:
        dump(statistica, file, ensure_ascii=False, indent=4, default=str)
