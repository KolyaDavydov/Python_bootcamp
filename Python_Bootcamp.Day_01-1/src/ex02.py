from typing import Dict
import ex00

def decorator(func):
    def wrapper(*args):
        print("SQUEAK")
        new_purse = func(*args)
        return new_purse
    return wrapper

@decorator
def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    return ex00.add_ingot(purse)

@decorator
def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    return ex00.get_ingot(purse)

@decorator
def empty(purse: Dict[str, int]) -> Dict[str, int]:
    return ex00.empty(purse)


if __name__ == "__main__":
    purse = {'gold_ingots': 10}
    print(purse)
    new_purse = add_ingot(get_ingot(add_ingot(empty(purse))))
    print(new_purse)