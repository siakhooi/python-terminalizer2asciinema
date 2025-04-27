from terminalizer2asciinema.util import get_arguments
from terminalizer2asciinema.terminalizer2asciinema import get_current_timestamp


def test_get_arguments():
    assert get_arguments(["hello.py", "arg1", "arg2"]) == ["arg1", "arg2"]


def test_get_current_timestamp():
    i = get_current_timestamp()
    assert type(i) is int
