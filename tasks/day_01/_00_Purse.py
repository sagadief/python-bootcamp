# import _02_Burglar_Alarm as dec
from _02_Burglar_Alarm import decorated_func

@decorated_func
def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    copy_purse = purse.copy()
    copy_purse['gold_ingots'] += 1
    return copy_purse

@decorated_func
def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    copy_purse = purse.copy()
    copy_purse['gold_ingots'] -= 1
    return copy_purse

@decorated_func
def empty(purse: dict[str, int]) -> dict[str, int]:
    copy_purse = purse.copy()
    if not copy_purse['gold_ingots']:
        copy_purse.update({'gold_ingots' : 0})
    else:
        copy_purse['gold_ingots'] = 0
    return copy_purse




if __name__ == "__main__":

    purse = {'gold_ingots' : 1}

    # print(add_ingot(get_ingot(add_ingot(empty(purse)))))
    print(add_ingot(purse))
    # print(purse)