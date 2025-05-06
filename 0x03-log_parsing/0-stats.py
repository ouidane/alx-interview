#!/usr/bin/python3
""" Reads stdin line by line and computes metrics. """
from datetime import datetime
from re import match
from sys import stdin
from typing import Sequence


def check_line(log_line: str) -> Sequence[int]:
    """ Checks line is right log format and returns two values from it """
    try:
        ip = match(r'\w.*\s*-\s*\[', log_line).span()[1]

        date = match(r'.*]', log_line[ip:]).span()[1]
        date_str = log_line[ip: ip + date].split('.')
        valid = str(datetime.strptime(date_str[0], '%Y-%m-%d %H:%M:%S'))
        if not (date_str[0] == valid and match(r'\d*', date_str[1]).span()[1]):
            raise AttributeError('Invalid date format!')

        req = match(' ?".*"', log_line[ip + date:]).span()[1]
        req_str = log_line[ip + date:][:req]
        if req_str[1:] != '"GET /projects/260 HTTP/1.1"':
            raise AttributeError('Invalid request string format!')

        status = match(r' \S*', log_line[ip + date + req:-1]).span()[1]
        status_str = log_line[ip + date + req:][1:status]
        status_str = int(status_str) if status_str.isnumeric() else 0

        size = match(r' \d*$', log_line[ip + date + req + status:]).span()[1]
        size_str = log_line[ip + date + req + status:][1:size]
        size_str = int(size_str) if size_str.isnumeric() else 0

        return status_str, size_str

    except (AttributeError, ValueError):
        pass

    return 0, 0


def log_parser() -> None:
    """ Parses lines from stdin and prints a summary every ten lines. """
    line = ' '
    lines, status_code, file_size, i = 1, 0, 0, 0
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    summary = {'codes': {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                         '404': 0, '405': 0, '500': 0},
               'size': 0}

    while line:
        skip, close = False, False
        try:
            line = stdin.readline()
            if not line:
                raise EOFError

            status_code, file_size = check_line(line)
            if not file_size:
                skip = True

        except (KeyboardInterrupt, EOFError):
            close = True
            break
        finally:
            if not close and not skip and file_size:
                summary['size'] += file_size
                if status_code in status_codes:
                    summary['codes'][str(status_code)] += 1
            if (lines and not lines % 10) or close:
                print(f'File size: {summary["size"]}')
                for key in sorted(summary['codes'].keys()):
                    if summary['codes'].get(key):
                        print(f'{key}: {summary["codes"][key]}')
            lines += 1


if __name__ == '__main__':
    log_parser()
