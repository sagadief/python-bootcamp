
def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    copy_purse = purse.copy()
    copy_purse['gold_ingots'] += 1
    return copy_purse

def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    copy_purse = purse.copy()
    copy_purse['gold_ingots'] -= 1
    return copy_purse

def empty(purse: dict[str, int]) -> dict[str, int]:
    copy_purse = purse.copy()
    if not copy_purse['gold_ingots']:
        copy_purse.update({'gold_ingots' : 0})
    else:
        copy_purse['gold_ingots'] = 0
    return copy_purse




if __name__ == "__main__":

    purse = {'gold_ingots':0}

    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
