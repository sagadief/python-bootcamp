import sys


def check_star(l):
    if l[0][0] == '*' and l[0][-1] == '*':
        if l[1][:2] == '**' and l[1][-2:] == '**':
            if l[2][0] == '*' and l[2][2] == '*' and l[2][4] == '*':
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_len(l):
    if len(l) == 3:
        for i in l:
            if len(i) != 5:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    m_file = open('m.txt', 'r')
    l = [line.strip() for line in m_file]

    counter = 0
    for i in l:
        for j in i:
            if j == '*':
                counter+=1

    if counter == 9 and check_star(l) and check_len(l):
        print(True)
    else:
        print(False)

    m_file.close()
