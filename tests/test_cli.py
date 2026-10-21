import json
from typer.testing import CliRunner
from streamstats.__main__ import app
runner = CliRunner()
def test_cli_csv_and_jsonl() -> None:
    """берет CSV и JSONL одновременно"""
    result = runner.invoke(app, ["tests/norm.csv", "tests/norm.jsonl", "--output", "tests/mix.json"])
    assert result.exit_code == 0


def test_unicode() -> None:
    """Кириллица не ломает программу"""
    result = runner.invoke(app, ["tests/norm.csv", "--output", "tests/unicode_report.json"])
    assert result.exit_code == 0
    with open("tests/unicode_report.json", encoding="utf-8") as f:
        report = json.load(f)
    assert report["total"] == 3

def test_cli_catalog(tmp_path) -> None:
    """CLI с временным каталогом"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("timestamp,level,source,message\n2024-01-01T10:00:00Z,INFO,api,test\n")
    output_file = tmp_path / "report.json"
    result = runner.invoke(app, [str(csv_file), "--output", str(output_file)])
    assert result.exit_code == 0
    assert output_file.exists()
