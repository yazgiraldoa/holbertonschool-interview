#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""


if __name__ == "__main__":
    import sys
    import signal

    def signal_handler(sig, frame):
        """Function to capture SIGINT signal"""
        print_output()

    def print_output():
        """Function to print the computed lines"""
        print("File size: {}".format(size))

        for key in sorted(status_codes.keys()):
            value = status_codes[key]
            if value == 0:
                continue
            print("{}: {}".format(key, value))

    status_codes = {
        "200": 0, "301": 0, "400": 0,
        "401": 0, "403": 0, "404": 0,
        "405": 0, "500": 0
        }
    line_number = 0
    size = 0

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        tokenized_in = line.split()
        line_number += 1

        try:
            size += int(tokenized_in[-1])
            status_codes[tokenized_in[-2]] += 1
        except Exception:
            continue

        if line_number % 10 == 0:
            print_output()

    if line_number == 0 or line_number % 10 != 0:
        print_output()
