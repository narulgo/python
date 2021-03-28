def best_student(students):
    maximum = 0
    for key, value in students.items():
        if value > maximum:
            maximum = value
            name = key
    return name

  
students_1 = {
  'Alice': 100,
  'Bob': 90,
  'Charlie': 80
}
students_2 = {
  'Anton': 100,
  'Barbara': 90,
  'Clarice': 80
}
students_3 = {
  'Alice': 50,
  'Bob': 10,
  'Charlie': 80,
  'David': 85
}

students_4 = {
  'Alice': 50,
  'Bob': 90,
  'Clarice': 100
}

students_5 = {
  'Alex': 50,
  'Bob': 90,
  'Clarice': 40
}

print(best_student(students_1))
print(best_student(students_2))
print(best_student(students_3))
print(best_student(students_4))
print(best_student(students_5))



assert best_student(students_1) == 'Alice'
assert best_student(students_2) == 'Anton'
assert best_student(students_3) == 'David'
assert best_student(students_4) == 'Clarice'
assert best_student(students_5) == 'Bob'

