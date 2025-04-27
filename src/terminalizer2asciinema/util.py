import time
from contextlib import contextmanager
import sys


def get_arguments(argv):
    return argv[1:]


def get_current_timestamp():

    return int(time.time())


@contextmanager
def stdin_manager():
    yield sys.stdin
