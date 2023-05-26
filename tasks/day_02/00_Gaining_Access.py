class Key:
    passphrase = "zax2rulez"

    # def __init__(self):
    #     pass
      
    def __len__(self):
        return 1337

    def __getitem__(self, value):
        return 3 if value == 404 else "err"

    def __str__(self) -> str:
        return "GeneralTsoKeycard"

    def __gt__(self, value):
        return value > 8999

if __name__ == "__main__":
    key = Key()
    print(len(key))
    print(key[404])
    print(key > 9000)
    print(key.passphrase)
    print(str(key))