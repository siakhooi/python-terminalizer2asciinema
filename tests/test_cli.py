from terminalizer2asciinema.cli import run
import pytest


def test_cli_run_wrong_arguments(monkeypatch):
    monkeypatch.setattr("sys.argv", ["terminalizer2asciinema", "x", "x"])

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_cli_run_wrong_file(monkeypatch):
    argv = ["terminalizer2asciinema", "/tmp/file-not-exists"]
    monkeypatch.setattr("sys.argv", argv)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2
