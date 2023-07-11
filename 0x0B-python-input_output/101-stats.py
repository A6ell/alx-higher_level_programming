#!/usr/bin/env python3
'''
script that reads stdin line by line
and computes metrics
'''


import sys


def print_statistics(total_size, status_codes):
    """Prints the computed statistics"""
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_codes.items()):
        print("{}: {}".format(status_code, count))


def parse_line(line):
    """Parses a log line and returns the file size and status code"""
    elements = line.split(" ")
    size = int(elements[-1])
    status_code = elements[-2]
    return size, status_code


def compute_metrics():
    """Reads stdin line by line and computes the metrics"""
    total_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            size, status_code = parse_line(line)
            total_size += size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise


compute_metrics()
