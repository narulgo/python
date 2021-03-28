import re


def find_dates(filename):
    numbers = file.read()
    numbers = re.findall(r'\d+[.]\d+[.]\d+', numbers)
    spisok = []
    for x in numbers:
        spisok.append(x)
    return spisok


file = open('date.txt')
date = find_dates(file)
print(date)
assert(date) == ['2018.10.01', '1984.05.06']


# date.txt


# 4545122113 eifheifheif 2018.10.01
# 1984.05.06 87845112 efefefef

