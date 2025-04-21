from terminalizer2asciinema.util import get_arguments


def test_get_arguments():
    assert get_arguments(['hello.py', 'arg1', 'arg2']) == ['arg1', 'arg2']
