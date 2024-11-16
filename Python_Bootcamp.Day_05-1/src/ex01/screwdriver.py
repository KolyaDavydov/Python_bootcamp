import argparse
import requests
from bs4 import BeautifulSoup
import os

URL = 'http://127.0.0.1:8888/'


def arg_parser():
    parser = argparse.ArgumentParser(description='Parser for localhost:8888')
    parser.add_argument(
        'action',
        choices=['upload', 'list'],
        help='Action to perform \
            ("upload": local file or "list": show uploaded files)'
    )
    parser.add_argument(
        'path',
        nargs='?',
        help='Path to the file to upload (only for "upload" action)'
    )
    return parser.parse_args()


# def get_list():


if __name__ == '__main__':
    args = arg_parser()
    if args.action == 'list':
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find('p', class_='audio')
                audio_list = [text for text in soup.stripped_strings]
                print(audio_list)
        except requests.exceptions.ConnectionError:
            print('\033[31mСервер не запущен или ошибка соединения\033[0m\nзапустите скрипт `flask_server.py` из другого теримнала')
    elif not os.path.exists(args.path):
        print('\033[31mТакого файла не существует\033[0m')
    else:
        with open(args.path, 'rb') as file:
            response = requests.post(URL, files={'file': file})
            print(response)
