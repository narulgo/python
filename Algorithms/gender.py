def approve(gender, age, score):
    result = True
    if score < 21:
        result = False

    if gender == 'F':
        if age >= 21 and age <= 39:
            score = score + 100
        if age >= 40:
            score = score + 50
        if gender == 'M':
            if age >= 21 and age <= 39:
                score = score + 50
            if age >= 40:
                score = score + 20
        if score > 500:
            result = True
        else:
            result = False
    return result


gender = input('Gender: ')
age = int(input('Age: '))
score = int(input('Score: '))

print(approve(gender, age, score))
