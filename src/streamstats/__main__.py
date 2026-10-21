from pathlib import Path
from typer import Exit, Option, Typer, echo
from .check import check
from .analysis import analys
from .constants import HELP
from .errors import StreamStatsError, UnsupportedFormatError
from .parsers import pars_csv, pars_json
from .report import save

app = Typer()

def parcing_events(paths: list[Path], skip_invalid: bool, skipped: dict[str, int]):
    """Читаем файлики и считаем количество пропущенных строк"""
    for path in paths:
        if path.suffix.lower() == ".csv":
            count = yield from pars_csv(path, skip_invalid)
            skipped["lines"] += count or 0
        elif path.suffix.lower() == ".jsonl":
            count = yield from pars_json(path, skip_invalid)
            skipped["lines"] += count or 0
        else:
            raise UnsupportedFormatError(f"Неподдерживаемый формат: {path.suffix}")


@app.command(help=HELP)
def main(file: list[Path],output: Path = Option(Path("report.json"), "--output"),skip_invalid: bool = Option(False, "--skip-invalid"),) -> None:
    """Запуск программы"""
    try:
        if check(file, output):
            skipped = {"lines": 0}
            statistics = analys(parcing_events(file, skip_invalid, skipped))
            statistics["skipped_lines"] = skipped["lines"]
            save(statistics, output)
    except StreamStatsError as error:
        echo(str(error), err=True)
        raise Exit(code=2)
if __name__ == "__main__":
    app()
