import xlsxwriter

entries = []
with open('parsed_info.txt', 'r') as file:
    entries = file.readlines()
   
data = list(map(eval, entries))


with xlsxwriter.Workbook('my_data.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(data):
        worksheet.write_row(row_num, 0, data)
    