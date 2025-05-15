#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """

import sys


def log(status, file_size):
    """
     Log the status and file size.

    Args:
        status (dict): A dictionary containing status codes and their counts.
        file_size (int): The size of the file to be logged.
    """
    print("File size: {}".format(file_size))
    for key, val in sorted(status.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size, counter = 0, 0
status = dict.fromkeys(
    ["200", "301", "400", "401", "403", "404", "405", "500"], 0
)

try:
    for line in sys.stdin:
        line = line.split()[::-1]
        if len(line) > 2:
            counter += 1
            if counter <= 10:
                file_size += int(line[0])
                if line[1] in status.keys():
                    status[line[1]] += 1
            if counter == 10:
                log(status, file_size)
                counter = 0

finally:
    log(status, file_size)
