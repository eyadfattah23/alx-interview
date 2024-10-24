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
import signal
import sys
import datetime

status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
counter = 1
Total_files_size = 0


def print_status_codes():
    """
    Print status codes and their counts in ascending order.
    """

    for key, value in status_codes.items():
        if value > 0:
            print(f'{key}: {value}')


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
    pattern = (r"^(?P<ip>([0-9]{1,3}\.){3}[0-9]{1,3}) - \[(?P<date>.+)\] "
               r"\"GET /projects/260 HTTP/1.1\" "
               r"(?P<status_code>\d{3}) (?P<file_size>\d+)$")

    re_obj = re.match(pattern, line)

    if re_obj:
        try:
            date_str = datetime.datetime.strptime(
                re_obj.group('date'), '%Y-%m-%d %H:%M:%S.%f')

            status_code = int(re_obj.group('status_code'))
            if status_code not in status_codes:
                return False
        except ValueError as VE:
            return False
        try:
            return {
                'ip': re_obj.group('ip'),
                'date': date_str,
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
            Total_files_size += parsed_line.get('file_size')
            status_codes[parsed_line.get('status_code')] += 1
            if counter % 10 == 0:
                print(f'File size: {Total_files_size}')
                print_status_codes()
            counter += 1
except KeyboardInterrupt:
    print(f'File size: {Total_files_size}')
    print_status_codes()
    raise
