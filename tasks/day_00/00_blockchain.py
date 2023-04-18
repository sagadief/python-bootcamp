import sys


def check_str(stroka):
    if len(stroka) == 32 and stroka.startswith('00000') and stroka[5] != 0:
        print(stroka)
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) == 2:
        for i in range(int(sys.argv[1])):
            s = input()
            check_str(s)