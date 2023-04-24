import _00_Purse as pur

def split_booty(*purse: dict[str, int]) -> dict[str, int]:
    copy_purse = tuple(purse)
    total_ingots = 0
    for d in copy_purse:
        total_ingots += d.get('gold_ingots', 0)

    purse_1, purse_2, purse_3 = {'gold_ingots': 0}, {'gold_ingots': 0}, {'gold_ingots': 0}

    lst = [purse_1, purse_2, purse_3]

    i = 0
    while total_ingots != 0:
        lst[i]['gold_ingots'] += 1
        total_ingots -= 1
        i += 1
        if i == 3:
            i = 0
    print(*lst)


if __name__ == "__main__":
    g1 = {'gold_ingots': 3}
    g2 = {'gold_ingots': 3}
    g3 = {'apples' : 10}
    g4 = {'gold_ingots': 4, 'apples' : 10}
    split_booty(g1, g2, g3, g4)