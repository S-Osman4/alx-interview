#!/usr/bin/python3
'''Module for log parsing script.'''

import sys

total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split(" ")
        if len(parts) != 9:
            continue
        ip, date, request, status_code, size = parts[0], parts[3], parts[5], int(parts[8]), int(parts[9])
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += size
        if line_count % 10 == 0:
            print("Total file size: ", total_size)
            for key in sorted(status_codes.keys()):
                print(key, ": ", status_codes[key])
except KeyboardInterrupt:
    print("Total file size: ", total_size)
    for key in sorted(status_codes.keys()):
        print(key, ": ", status_codes[key])
