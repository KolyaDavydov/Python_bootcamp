"""Exercise 02: Track and Capture
Для запуска скрипта в терминале ввести:
`cat not_m.txt | python3 mfinder.py`
"""

import argparse
import sys
import re

parser = argparse.ArgumentParser(description='Find M, ex02. No arguments required')
parser.parse_args()

if __name__ == '__main__':
    input_all_lines = sys.stdin.read()
    if re.fullmatch(r'.{5}\n.{5}\n.{5}\n*', input_all_lines) is None:
        print("Error")
    elif re.fullmatch(r'\*[^*][^*][^*]\*\n\*\*[^*]\*\*\n\*[^*]\*[^*]\*\n*',
                      input_all_lines) is None:
        print("False")
    else:
        print("True")
