import openpyxl

filename = "result_highlights_updateddata.xlsx"

wb = openpyxl.load_workbook(filename)
sheet = wb.active

for _ in range(87):
  index = _ + 1
  cell = sheet.cell(row = index, column = 1)

  text_file = open("results/doc_" + str(index) + ".txt", "w")
  text_file.write(cell.value)
  text_file.close()