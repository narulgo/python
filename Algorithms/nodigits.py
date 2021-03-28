def nodigits(string):
    no_digits = []
    for i in string:
        if not i.isdigit():
            no_digits.append(i)
    result = ''.join(no_digits)
    return result


string = 'Al5ice is 20 years 99 old'
print(nodigits(string))
#assert nodigits('Alice is 20 years old') == 'Alice is  years old'
#assert nodigits('Alice is 20 years 99 old') == 'Alice is  years  old'
assert nodigits('Al5ice is 20 years 99 old') == 'Alice is  years  old'
