import sys
import os
from termcolor import colored
import yaml
import json


def error(s):
    print(colored(s, "red"))


def get_current_timestamp():
    import time

    return int(time.time())


def convert(inputfile):

    if not os.path.exists(inputfile):
        error(f"{inputfile} is not exist.")
        sys.exit(2)

    output = []

    with open(inputfile, "r") as f:
        data = yaml.safe_load(f)
        width = data["config"]["cols"]
        height = data["config"]["rows"]

    timestamp = get_current_timestamp()

    output.append(
        {
            "version": 2,
            "width": width,
            "height": height,
            "timestamp": timestamp,
            "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"},
        }
    )

    event_stream_time = 0.0
    for record in data["records"]:
        event_stream_time += record["delay"] / 1000.0
        event_stream_time = round(event_stream_time, 6)
        output.append([event_stream_time, "o", record["content"]])

    for line in output:
        print(json.dumps(line))
