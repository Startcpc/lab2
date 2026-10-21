from pathlib import Path
from typer import Typer, Option, echo, Exit
from .constants import HELP
from .parsers import pars_csv, pars_json
from .analysis import analys
from .report import save
from .errors import StreamStatsError, ConfigurationError, UnsupportedFormatError

app = Typer()

@app.command(help=HELP)
def main(file: list[Path],output: Path = Option(Path("report.json"), "--output"),skip_invalid: bool = Option(False, "--skip-invalid"),) -> None:
    """Принимает команды,обрабатывает их, и делает отчёт"""
    events = []
    skipped_lines = 0
    try:
        if any(path.resolve() == output.resolve() for path in file):
            raise ConfigurationError("Ошибка конфигурации CLI")
        for path in file:
            if path.suffix.lower() == ".csv":
                parsed_events, skipped = pars_csv(path, skip_invalid)
                events.extend(parsed_events)
                skipped_lines += skipped
            elif path.suffix.lower() == ".jsonl":
                parsed_events, skipped = pars_json(path, skip_invalid)
                events.extend(parsed_events)
                skipped_lines += skipped
            else:
                raise UnsupportedFormatError(f"Неподдерживаемый формат: {path.suffix}")

        statistics = analys(events, skipped_lines)
        save(statistics, output)

    except StreamStatsError as error:
        echo(str(error), err=True)
        raise Exit(code=2)


if __name__ == "__main__":
    app()
