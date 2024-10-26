#!/usr/bin/python3
"""
Interview Preparation (stats)
"""
import sys
import re
import signal

status_codes = {}
total_file_size = 0


def updater(code, size):
    global total_file_size

    if code in [200, 301, 400, 401, 403, 404, 405, 500]:
        status_codes[code] = status_codes.get(code, 0) + 1
        total_file_size += size


def displayer(signum=None, frame=None):
    print(f"File size: {total_file_size}")
    for s_code in sorted(status_codes):
        print(f"{s_code}: {status_codes[s_code]}")


signal.signal(signal.SIGINT, displayer)

log_pattern = re.compile(r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

line_counter = 0
for line in sys.stdin:
    match = log_pattern.match(line.strip())
    if match:
        code, size = int(match.group(1)), int(match.group(2))
        updater(code, size)
        line_counter += 1

    if line_counter % 10 == 0:
        displayer()

displayer()
