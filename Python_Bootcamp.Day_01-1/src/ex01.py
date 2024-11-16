from typing import Dict


def split_booty(*purses: Dict[str, int]):
    gold_count = 0
    for purse in purses:
        if 'gold_ingots' in purse:
            gold_count += purse['gold_ingots']

    purses_with_gold = list()

    purses_with_gold.append({'gold_ingots': gold_count // 3})
    gold_count -= gold_count // 3

    purses_with_gold.append({'gold_ingots': gold_count // 2})
    gold_count -= gold_count // 2

    purses_with_gold.append({'gold_ingots': gold_count})

    return purses_with_gold[0], purses_with_gold[1], purses_with_gold[2]

if __name__ == "__main__":
    purses = split_booty({"gold_ingots":3}, {"gold_ingots" :2}, {"apples":10})
    print('test_1:', purses)

    purses = split_booty({"orange":3}, {"gold_ingots" :2}, {"apples":10})
    print('test_2:', purses)

    purses = split_booty({"orange":3}, {"gold" :2}, {"apples":10})
    print('test_3:', purses)

    purses = split_booty({}, {"gold_ingots" :745}, {"apples":10})
    print('test_4:', purses)