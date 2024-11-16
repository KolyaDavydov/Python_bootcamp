from typing import Dict

def add_ingot(purse: Dict[str, int]) -> Dict[str,int]:
    new_purse = purse.copy()
    if 'gold_ingots' in new_purse:
        new_purse['gold_ingots'] += 1
    else:
        new_purse['gold_ingots'] = 1
    return new_purse

def get_ingot(purse: Dict[str, int]) -> Dict[str,int]:
    new_purse = purse.copy()
    if 'gold_ingots' in new_purse:
        if new_purse['gold_ingots'] > 0:
            new_purse['gold_ingots'] -= 1
    return new_purse

def empty(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse = purse.copy()
    new_purse.clear()
    return new_purse


if __name__ == "__main__":
    purse = {'gold_ingots': 10}
    new_purse = add_ingot(get_ingot(add_ingot(empty(purse))))
    print(new_purse)
