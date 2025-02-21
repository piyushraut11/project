import openpyxl

wb = openpyxl.load_workbook(r"C:\Users\dhana\Downloads\Excel_exercise.xlsx")

sheet1 = wb['Sheet1']
print(sheet1)
#sheet2 = wb['']
