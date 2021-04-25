from openpyxl import Workbook
import time
import random
import pandas as pd

excel = Workbook()
sheet = excel.active

sheet['A1'] = "Student Name"
sheet['B1'] = "College"
sheet['C1'] = "Age"
sheet['D1'] = "Grade"

Column_1 = ['Tom', 'Tina', 'Joseph', 'George', 'Ram', 'Arif', 'Vidya', 'Christine', 'Ramya', 'Edwin']

for j in range(2,22):
    sheet['A'+str(j)] = random.choice(Column_1)

College_names = ['Loyola', 'WCC', 'MCC', 'Madras University', 'Harvard', 'Standford', 'RMK', 'Anna University', 'Oxford', 'SMU']

for k in range(2,22):
    sheet['B'+str(k)] = random.choice(College_names)

for l in range(2,22):
    sheet['C'+str(l)] = random.randrange(22, 26,1)

for m in range(2,22):
    sheet['D'+str(m)] = random.randrange(4, 10,1)

excel.create_sheet('Pivot Table')
excel.save("pivot.xlsx")
print('created')
dff = pd.read_excel("pivot.xlsx")
pivot = pd.pivot_table(dff, index = ["Student Name", "College"])
pivot = pd.pivot_table(pivot, index = ["Student Name", "College"])
print(pivot)
pivot.to_excel("pivot_table.xlsx", sheet_name = 'Pivot Table')


