from openpyxl import Workbook
import time

excel = Workbook()
sheet = excel.active

Column_1 = ['Name', 'Jay', 'Nick', 'Mike', 'Tina', 'Vikas']
Column_2 = ['Address', 'Bangalore', 'London', 'Chikago', 'Pune', 'Delhi']
Column_3 = ['Organization', 'SeaportAI', 'Company A', 'Company B', 'Company C', 'Company D']

for i in range(1,7):
    sheet['A'+str(i)] = Column_1[i-1]

for j in range(1,7):
    sheet['B'+str(j)] = Column_2[j-1]

for k in range(1,7):
    sheet['C'+str(k)] = Column_3[k-1]
excel.save('excel.xlsx')
print('file was created')