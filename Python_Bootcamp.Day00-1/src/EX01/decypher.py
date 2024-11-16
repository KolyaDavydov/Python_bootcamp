"""Exercise 01: Decypher
Для запуска скрипта в терминале ввести:
`python3 decypher.py "Have you delivered eggplant pizza at restored keep?"`
"""
import sys
import argparse


parser = argparse.ArgumentParser(description='script to decipher the sentence')
parser.add_argument('numoflines', type=str, help='sentence')
args = parser.parse_args()

if __name__ == '__main__':
    line = sys.argv[1]
    words = line.split()
    answer = ""
    for word in words:
        answer += word[0]
    print(answer)
