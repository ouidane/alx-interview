#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

# Only track these specific status codes
valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}


def print_stats():
    """Prints the file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(valid_status_codes):
        if status_counts[code]:
            print(f"{code}: {status_counts[code]}")


def parse_line(line):
    """Parses a log line and returns status code and file size if valid."""
    try:
        parts = line.strip().split()
        # Expected format:
        # IP - [date] "GET /projects/260 HTTP/1.1" status_code file_size
        if len(parts) < 7:
            return None, None
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code not in valid_status_codes:
            return None, None
        return status_code, int(file_size)
    except (IndexError, ValueError):
        return None, None


try:
    for line in sys.stdin:
        status_code, file_size = parse_line(line)
        if status_code and file_size is not None:
            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
except Exception:
    pass
else:
    print_stats()
