#!/usr/bin/env python3
"""
script that reads stdin line by line
and computes metrics
"""


import sys


def print_statistics(file_size, status_codes):
    """Prints the computed statistics"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes):
        count = status_codes[code]
        print("{}: {}".format(code, count))


def compute_metrics():
    """Reads stdin line by line and computes the metrics"""
    file_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1

            ip, _, date, request, status, size = line.split(" ", 5)
            file_size += int(size)

            if status in status_codes:
                status_codes[status] += 1
            else:
                status_codes[status] = 1

            if line_count % 10 == 0:
                print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)
        raise


compute_metrics()
