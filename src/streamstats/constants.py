from typing import Literal

HELP = """\b
Примеры использования:
  python -m streamstats analyze events.csv --format csv
  python -m streamstats analyze events.jsonl --format jsonl
  python -m streamstats analyze events.csv events.jsonl --format csv --output result.json
  python -m streamstats analyze events.csv --format csv --skip-invalid
  python -m streamstats analyze events.csv --format csv --output report.csv --csv
Справка:
  python -m streamstats --help
\b

"""
CRITICAL_LEVELS = ("ERROR", "CRITICAL")
VALID_LEVEL = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
