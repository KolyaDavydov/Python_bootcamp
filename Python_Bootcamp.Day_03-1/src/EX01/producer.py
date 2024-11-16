"""Скрипт использует redis в качетсве очереди сообщений
В данном случае скрипт создает 6 сообщений в формате json
и передает как очередь в redis
"""

import logging
from random import randint
import json
import redis  # 'sudo pip3 install redis' Для ubunta 20.04


def create_logging() -> None:
    logging.basicConfig(level=logging.DEBUG)


def create_database() -> redis.Redis:
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.flushall()
    return r


def create_and_push_data_to_redis_db(r: redis.Redis) -> None:
    account_numbers = [1_000_000_000,
                       1_111_111_111,
                       2_000_000_000,
                       2_222_222_222,
                       3_000_000_000,
                       3_333_333_333,
                       4_000_000_000,
                       4_444_444_444,
                       5_000_000_000,
                       5_555_555_555]

    for i in range(0, len(account_numbers), 2):
        transaction = {"metadata": {"from": account_numbers[i], "to": account_numbers[i + 1]},
                       "amount": randint(-10_000, 10_000)}

        logging.info(transaction)
        r.publish('chanel_1', message=json.dumps(transaction))


if __name__ == '__main__':
    create_logging()
    r = create_database()
    create_and_push_data_to_redis_db(r)
