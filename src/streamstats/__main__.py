from pathlib import Path
from typer import Exit, Option, Typer, echo
from streamstats.check import check
from streamstats.analysis import analys
from streamstats.errors import StreamStatsError, UnsupportedFormatError, EmptyFileError
from streamstats.parsers import pars_csv, pars_jsonl
from streamstats.report import save, save_csv
from streamstats.constants import HELP

app = Typer(help=HELP)


def parcing_events(
    paths: list[Path], fmt: str, skip_invalid: bool, skipped: dict[str, int]
):
    for path in paths:
        if fmt == "csv":
            count = yield from pars_csv(path, skip_invalid)
            skipped["lines"] += count or 0
        elif fmt == "jsonl":
            count = yield from pars_jsonl(path, skip_invalid)
            skipped["lines"] += count or 0
        else:
            raise UnsupportedFormatError(f"Неподдерживаемый формат: {fmt}")


@app.command("analyze", help=HELP)
def main(
    file: list[Path],
    format: str = Option(..., "--format"),
    output: Path = Option(Path("report.json"), "--output"),
    skip_invalid: bool = Option(False, "--skip-invalid"),
    csv: bool = Option(False, "--csv"),
) -> None:
    """Главная функция -> точка входа"""
    try:
        check(file, output)
        skipped = {"lines": 0}
        statistics = analys(parcing_events(file, format, skip_invalid, skipped))
        statistics["skipped_lines"] = skipped["lines"]
        if statistics["total"] == 0:
            raise EmptyFileError("Файл пустой")
        if csv:
            save_csv(statistics, output)
        else:
            save(statistics, output)
    except StreamStatsError as error:
        echo(str(error), err=True)
        raise Exit(code=2)


@app.command(hidden=True)
def mem() -> None:
    """Скрытая команда,нужна для корректной работы команд в Тайпер(минимум две команды нужно)"""


if __name__ == "__main__":
    app()
