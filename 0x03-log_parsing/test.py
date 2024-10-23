#!/usr/bin/python3


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


def print_status_codes():
    for key, value in status_codes.items():
        print(f'{key}: {value}')


lines = []
counter = 0
Total_files_size = 0


def match_parse_line(line):
    if not line or line == '' or line == '\n':
        return False

    pattern = r"^(?P<ip>([0-9]{1,3}\.){3}[0-9]{1,3}) - \[(?P<date>.+)\]\s\"GET /projects/260 HTTP/1.1\"\s(?P<status_code>\d{3})\s(?P<file_size>\d+)$"

    re_obj = re.match(pattern, line)

    if re_obj:
        try:
            date_str = datetime.datetime.strptime(
                re_obj.group('date'), '%Y-%m-%d %H:%M:%S.%f')

        except ValueError as VE:
            return False
        try:
            return {
                'ip': re_obj.group('ip'),
                'date': date_str,
                'status_code': int(re_obj.group('status_code')),
                'file_size': int(re_obj.group('file_size')),
            }
        except Exception as E:
            return False

    return False


def interrupt_handler(signum, frame):
    print(f'File size: {Total_files_size}')


signal.signal(signal.SIGINT, interrupt_handler)


for line in sys.stdin:
    parsed_line = match_parse_line(line)

    if parsed_line:
        Total_files_size += parsed_line.get('file_size')
        status_codes[parsed_line.get('status_code')] += 1
        if counter % 10 == 0:
            print(f'File size: {Total_files_size}')
            print_status_codes()
        counter += 1
