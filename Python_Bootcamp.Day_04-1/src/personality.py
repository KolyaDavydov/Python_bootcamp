from random import randint


'''
Генерирует список целых неотрицательных чисел от 0 до 100
с общей суммой равной 100'''
def number_list_generator() -> []:
    list_value: list = []
    sum_value: int = 0
    for i in range(4):
        list_value.append(randint(0, 100 - sum_value))
        sum_value += list_value[i]
    list_value.append(100 - sum_value)
    return list_value


'''
Динамически генерирует класс Turret и возвращает объект этого класса'''
def turrets_generator():
    personality_traits: list = ['neuroticism', 'openness', 'conscientiousness', 'extraversion', 'agreeableness']
    turrets: dict = dict(zip(personality_traits, number_list_generator()))

    def shoot():
        print("Shooting")

    def search():
        print("Searching")

    def talk():
        print("Talking")

    turret_action: dict = {
        'shoot': shoot,
        'search': search,
        'talk': talk
    }

    return type('Turrer', (object, ), turrets | turret_action)


if __name__ == '__main__':
    turret = turrets_generator()

    print("\033[0m\033[32m____тип динамически сгенерированного объекта____\033[0m")
    print(type(turret))
    print()

    print("\033[0m\033[32m____Методы класса 'Turret'____\033[0m")
    turret.shoot()
    turret.search()
    turret.talk()
    print()

    print("\033[0m\033[32m____Значение атрибутов класса 'Turret'____\033[0m")
    print('neuroticism: ', turret.neuroticism)
    print('openness: ', turret.openness)
    print('conscientiousness: ', turret.conscientiousness)
    print('extraversion: ', turret.extraversion)
    print('agreeableness: ', turret.agreeableness)

    print()

    print("\033[0m\033[32m____Сумма атрибутов класса 'Turret'____\033[0m")
    print(turret.neuroticism +
          turret.openness +
          turret.conscientiousness +
          turret.extraversion +
          turret.agreeableness)
