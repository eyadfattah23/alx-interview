#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics based on log entries.
It processes lines that match the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
It calculates:
- Total file size.
- Number of lines per status code.
"""


import re
import time
import sys
import datetime

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
counter = 1
total_files_size = 0


def print_status_codes():
    """Print the status codes in sorted order."""
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def match_parse_line(line):
    """
    Parse the input log line to extract information such as:
    - IP address
    - Date
    - Status code
    - File size

    :param line: Single line of log entry
    :return: Parsed data as a dictionary, or False if format is invalid.
    """

    if not line or line == '' or line == '\n':
        return False

    # Regular expression pattern for log entry
    pattern = (r"^(?P<ip>.+\s*-\s*\[(?P<date>.+)\]\s*"
               r"\"GET /projects/260 HTTP/1.1\" "
               r"(?P<status_code>\d{3}) (?P<file_size>\d+)$")

    re_obj = re.match(pattern, line)

    if re_obj:
        try:
            status_code = re_obj.group('status_code')
            if status_code not in status_codes:
                return False
        except ValueError as VE:
            return False
        try:
            return {
                'ip': re_obj.group('ip'),
                'date': re_obj.group('date'),
                'status_code': status_code,
                'file_size': int(re_obj.group('file_size')),
            }
        except Exception as E:
            return False

    return False


"""
def interrupt_handler(signum, frame):
    print(f'File size: {Total_files_size}')
    print_status_codes()


signal.signal(signal.SIGINT, interrupt_handler) """

try:
    for line in sys.stdin:
        parsed_line = match_parse_line(line)

        if parsed_line:
            total_files_size += parsed_line.get('file_size')
            status_codes[parsed_line.get('status_code')] += 1
            if counter % 10 == 0:
                print('File size: {}'.format(total_files_size))
                print_status_codes()
            counter += 1

    print(f'File size: {total_files_size}')
    print_status_codes()
except KeyboardInterrupt:
    print(f'File size: {total_files_size}')
    print_status_codes()
    raise
