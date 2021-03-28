def avg_grade(students):
  result = {}
  for name, subjects in students.items():
    result[name] = {}
    for subject, grades in subjects.items():
      for grade in grades:
        avggr = sum(grades) / len(grades)
        result[name][subject] = avggr
  return result


def build_avg_grade_dict(students):
  students_with_avg_grade = avg_grade(students)
  result = {}
  for student_name, subjects in students_with_avg_grade.items():
    avg = 0
    length = 0
    for subject in subjects.values():
      avg += subject
      length = (len(subjects))
      result[student_name] = avg / length
  return result

students_1 = {
  'Alice': {
    'math': [100, 100, 100],
  },
  'Bob': {
    'math': [50, 50],
  },
  'Charlie': {
    'physics': [80]
  }
}

students_2 = {
  'David': {
    'math': [100, 100, 100],
    'biology': [100, 100, 100],
    'history': [50, 50, 50, 100]
  },
  'Ethan': {
    'math': [50, 50],
    'history': [100, 100]
  }
}


print(build_avg_grade_dict(students_1))
print(build_avg_grade_dict(students_2))

assert build_avg_grade_dict(students_1) == {'Alice': 100.0, 'Bob': 50.0, 'Charlie': 80.0}
assert build_avg_grade_dict(students_2) == {'David': 87.5, 'Ethan': 75.0}
