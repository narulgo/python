
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

def avg_grade(students):
  result = {}
  for name, subjects in students.items():
    result[name] = {}
    for subject, grades in subjects.items():
      avggr = sum(grades) / len(grades)
      result[name][subject] = avggr
  return result

def best_by_avg_grade(students):
  result = {}
  for student_name, subjects in students.items():
    for subject, grade in subjects.items():
      if subject not in result or result[subject]['grade'] < grade:
        result[subject] = {
          'name': student_name,
          'grade': grade
        }
           
  return result

def best(students):
  students_with_avg_grade = avg_grade(students)
  best_student_by_subject = best_by_avg_grade(students_with_avg_grade)
  total_result = {}
  for subject, student in best_student_by_subject.items():
    total_result[subject] = student['name']
  return total_result



print(best(students))

