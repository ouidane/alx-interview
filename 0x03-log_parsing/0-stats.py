#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys
import re
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Prints accumulated metrics"""
    print(f"File size: {total_size}")
    for code in sorted(valid_status_codes):
        if status_counts[code]:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        match = pattern.match(line.strip())
        if match:
            status_code, file_size = match.group(2), match.group(3)
            try:
                total_size += int(file_size)
                if status_code in valid_status_codes:
                    status_counts[status_code] += 1
            except ValueError:
                pass
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
else:
    print_stats()
