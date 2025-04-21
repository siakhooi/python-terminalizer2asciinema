from terminalizer2asciinema.terminalizer2asciinema import convert
from terminalizer2asciinema.terminalizer2asciinema import get_current_timestamp
import terminalizer2asciinema
import pytest


def test_convert_missing_file():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        convert("/tmp/file-not-exists")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_convert_correct_file(capsys, monkeypatch):
    def mock_timestamp():
        return 1745223672

    monkeypatch.setattr(
        terminalizer2asciinema.terminalizer2asciinema,
        "get_current_timestamp",
        mock_timestamp,
    )

    output_file = "tests/test-data/expected-output.txt"
    with open(output_file, "r") as file:
        expected_output = file.read()

    convert("tests/test-data/test-data.yml")
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_get_current_timestamp():
    i = get_current_timestamp()
    assert type(i) is int
