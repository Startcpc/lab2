from json import dump
from pathlib import Path
from csv import DictWriter


def save(data: dict, output: Path) -> None:
    """Записываем отчёт в jsonфайлик"""
    with Path(output).open("w", encoding="utf-8") as file:
        dump(data, file, ensure_ascii=False, indent=2, default=str)


def save_csv(data: dict, output: Path) -> None:
    """Записываем в CSV файлик"""
    with Path(output).open("w", encoding="utf-8", newline="") as file:
        writer = DictWriter(
            file,
            fieldnames=[
                "total",
                "levels",
                "source",
                "top_5",
                "first_time_event",
                "last_time_event",
                "skipped_lines",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "total": data["total"],
                "levels": str(data["levels"]),
                "source": str(data["source"]),
                "top_5": str(data["top_5"]),
                "first_time_event": data["first_time_event"],
                "last_time_event": data["last_time_event"],
                "skipped_lines": data["skipped_lines"],
            }
        )
