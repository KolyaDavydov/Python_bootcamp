class Key:
    def __init__(self) -> None:
        self.passphrase = 'zax2rules'

    def __str__(self) -> str:
        return 'GeneralTsoKeycard'
    
    def __len__(self) -> int:
        return 1337
    
    def __gt__(self, other: int) -> bool:
        return other < 9001
    
    def __getitem__(self, key: int) -> int:
        if key == 404:
            return 3
        else:
            return 1
        


if __name__ == '__main__':
    key = Key()
    print(len(key))
    print(key[404])
    print(key > 9000)
    print(key.passphrase)
    print(str(key))