
def avg_grade(student, subject):
    sum_of_grages = 0
    for grades in student[subject]:
        sum_of_grages += grades
    mid_grade = sum_of_grages / len(student[subject])
    return mid_grade


alice = {'math': [100, 100, 100], 'biology': [100, 100, 100],
'history': [90, 100]}
bob = {'math': [50, 50], 'history': [100, 100]}


print(avg_grade(alice, 'math'))
print(avg_grade(alice, 'biology'))
print(avg_grade(alice, 'history'))
print(avg_grade(bob, 'math'))
print(avg_grade(bob, 'history'))


assert avg_grade(alice, 'math') == 100.0
assert avg_grade(alice, 'biology') == 100.0
assert avg_grade(alice, 'history') == 95.0
assert avg_grade(bob, 'math') == 50.0
assert avg_grade(bob, 'history') == 100.0


