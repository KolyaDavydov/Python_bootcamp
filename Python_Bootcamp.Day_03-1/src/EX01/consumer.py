"""скрипт для чтения сообщений из redis
    Сначал запускаем этот скрипт с аргументами, напрпимер:
    'python3 consumer.py -e 1111111111,2222222222,1000000000,20000000000'

    Затем в другом терминале запускаем скрипт `python3 producer.py`
В Этот скрипт будет слушать redis. Как только в redis поступает сообщение (producer.py)
Данный скрипт будет проверять сообщение и выводить его или в оригинале  или с корректировкой
Данный скрипт явялется слушателем и для выхода из режима слушателя нажать `ctrl+C`
"""
import redis
import argparse
import json
import logging
import time

r = redis.Redis(host='localhost', port=6379, db=0)

parser = argparse.ArgumentParser()
parser.add_argument('-e', help="List of bad guys accounts", required=True)
args = parser.parse_args()

bad_gays = [int(account) for account in args.e.split(',')]

consumer = r.pubsub()
consumer.subscribe('chanel_1')
logging.basicConfig(level=logging.DEBUG)

# цикл для того что бы дождаться передачи данных в redis
while True:
    message = consumer.get_message()
    if message and message.get("data", 0):
        break
    time.sleep(0.01)

while True:
    message = consumer.get_message()
    if message:
        payload = json.loads(message.get("data", 0))
        if payload['amount'] > 0 and payload['metadata']['to'] in bad_gays:
            payload['metadata']['to'], payload['metadata']['from'] = payload['metadata']['from'], payload['metadata'][
                'to']
        logging.info(payload)
    time.sleep(0.1)
