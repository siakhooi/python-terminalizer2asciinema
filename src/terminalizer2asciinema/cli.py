import sys
from terminalizer2asciinema.terminalizer2asciinema import convert
from terminalizer2asciinema.util import get_arguments


def run():
    argv = get_arguments(sys.argv)
    if len(argv) > 1:
        print("Usage: terminalizer2asciinema [terminalizer_file]")
        sys.exit(1)
    elif len(argv) == 0:
        inputfile = None
    else:
        inputfile = argv[0]
    convert(inputfile)
