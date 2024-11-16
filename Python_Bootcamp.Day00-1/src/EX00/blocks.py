"""Exercise 00: Blockchain
Для запуска скрипта в терминале ввести:
`cat data_hashes_10lines.txt | python3 blocks.py 10`
"""
import sys
import argparse

parser = argparse.ArgumentParser(description='Script fo parser lines in stdin')
parser.add_argument('numlines', type=int, help='Num of lines in stdin')
args = parser.parse_args()


def check_line(line):
    if len(line) != 32:
        return False
    if line[0:5] == "00000" and line[5] != '0':
        return True
    return False


if __name__ == '__main__':
    for i in range(int(sys.argv[1])):
        line = sys.stdin.readline()
        if check_line(line.rstrip('\n')):
            print(line.rstrip('\n'))
