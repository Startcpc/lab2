from typing import Literal

HELP = """\bПримеры использования:
  python -m streamstats events.csv
  python -m streamstats events.jsonl
  python -m streamstats events.csv events.jsonl
  python -m streamstats events.csv --output result.json
\bСправка:
  python -m streamstats --help
"""

CRITICAL_LEVELS = ["ERROR", "CRITICAL"]
VALID_LEVEL = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
