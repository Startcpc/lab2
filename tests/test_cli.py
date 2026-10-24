from json import load
from typer.testing import CliRunner
from streamstats.__main__ import app

runner = CliRunner()


def test_cli_many_files() -> None:
    """берет несколько файлов одного формата"""
    result = runner.invoke(
        app,
        [
            "analyze",
            "tests/norm.csv",
            "tests/norm.csv",
            "--format",
            "csv",
            "--output",
            "tests/multi_report.json",
        ],
    )
    assert result.exit_code == 0
    with open("tests/multi_report.json", encoding="utf-8") as f:
        report = load(f)
    assert report["total"] == 6


def test_unicode() -> None:
    """Кириллица не ломает программу"""
    result = runner.invoke(
        app,
        [
            "analyze",
            "tests/norm.csv",
            "--format",
            "csv",
            "--output",
            "tests/unicode_report.json",
        ],
    )
    assert result.exit_code == 0
    with open("tests/unicode_report.json", encoding="utf-8") as f:
        report = load(f)
    assert report["total"] == 3


def test_cli_catalog(tmp_path) -> None:
    """CLI с временным каталогом"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        "timestamp,level,source,message\n2024-01-01T10:00:00Z,INFO,api,test\n"
    )
    output_file = tmp_path / "report.json"
    result = runner.invoke(
        app, ["analyze", str(csv_file), "--format", "csv", "--output", str(output_file)]
    )
    assert result.exit_code == 0
    assert output_file.exists()
