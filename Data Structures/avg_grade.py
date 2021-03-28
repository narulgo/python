
def avg_grade(student):
    sum_of_grades = 0
    length_of_grades = 0
    for subjects in student.keys():
        for grade in student[subjects]:
            sum_of_grades += grade
        length_of_grades += len(student[subjects])
    return sum_of_grades / length_of_grades


alice = {'math': [100, 100, 100], 'biology': [100, 100, 100],
'history': [50, 50, 50, 100]}
bob = {'math': [50, 50], 'history': [100, 100]}


print(avg_grade(alice))
print(avg_grade(bob))


assert avg_grade(alice) == 85.0
assert avg_grade(bob) == 75.0
