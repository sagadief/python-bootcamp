import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        for i in range(int(sys.argv[1])):
            s = input()
            s = [i[:1] for i in s.split()]
            print(''.join(s))