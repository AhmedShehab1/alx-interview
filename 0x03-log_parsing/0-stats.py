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

for i, line in enumerate(sys.stdin):
    results = re.findall(r"\d{3}\s\d{1,4}", line.strip())
    if results:
        code, size = results[0].split(" ")
        updater(int(code), int(size))
    if (i + 1) % 10 == 0:
        displayer()

