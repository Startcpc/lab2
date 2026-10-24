from streamstats.errors import ConfigurationError
from pathlib import Path


def check(paths: list[Path], output: Path) -> None:
    """Проверяет входных данных"""
    if not paths:
        raise ConfigurationError("Не указаны входные файлы")
    if any(not p.is_file() for p in paths):
        raise ConfigurationError("Либо файла нет, либо ты ввёл неправильный путь")
    output_path = output.resolve()
    if any(path.resolve() == output_path for path in paths):
        raise ConfigurationError("Входной и отчетный файл совпадают")
    if output.suffix.lower() != ".json" and output.suffix.lower() != ".csv":
        raise ConfigurationError("Выходной файл должен быть json или csv")
