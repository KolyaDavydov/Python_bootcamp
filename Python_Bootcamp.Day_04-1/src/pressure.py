from random import randint
from time import sleep


def emit_gel(step=50):
    pressure = 21
    while True:
        current_step = randint(0, step)
        sign = yield pressure
        pressure += sign * current_step
        if pressure < 0:
            pressure = 0
        if pressure > 100:
            pressure = 100


def valve(generator):
    sign = 1
    pressure = next(generator)
    while True:
        if pressure <= 10 or pressure >= 90:
            print("\033[31mДавление: ", pressure, "\033[0m")
            print("\033[1m\033[31m____Опасное давления! остановка!____\033[0m")
            generator.close()
            break
        if pressure < 20 or pressure > 80:
            print("\033[33mДавление: ", pressure, "\033[0m")
            print("\033[1m\033[33m____Критическое давление. Разворот шага____\033[0m")
            sign = -sign
        else:
            print("\033[32mДавление: ", pressure, "\033[0m")

        pressure = generator.send(sign)
        sleep(0.2)


if __name__ == '__main__':
    gen = emit_gel(30)
    valve(gen)
