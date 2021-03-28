
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
      mid = avg / length
      result[student_name] = mid
  for key, value in result.items():
    if value > mid:
      return key


students = {
    'Alice': {
        'math': [100, 100, 100],
        'biology': [100, 100, 100],
        'history': [90, 100]
    },
    'Bob': {
        'math': [50, 50],
        'history': [100, 100]
    }
}


print(build_avg_grade_dict(students))

