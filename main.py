import requests
import json
import openpyxl

json_file_path = "E:/lis-to-tm/result.json"

def print_hi():
    with open("result.json",encoding='utf-8', errors='ignore') as file:
        data = json.load(file,strict=False)
    req = requests.get(url='https://market.csgo.com/api/v2/prices/RUB.json')
    items = req.json()['items']
    book = openpyxl.Workbook()
    sheet = book.active
    sheet['A1'] = 'name'
    sheet['B1'] = 'lis price'
    sheet['C1'] = 'tm price'
    sheet['D1'] = 'profit s 10%'
    sheet['E1'] = 'procent'
    row = 2
    for item in items:
        for item2 in data:
            if (item['market_hash_name'] == item2['market_hash_name']):
                sheet[row][0].value = item2['market_hash_name']
                a = item2['price']
                b = a.split()
                b = ''.join(b)
                c = item['price']
                k = c.split()
                k = ''.join(k)
                raznica = float((float(b) - float(k)) * 0.9)
                procent = float(((float(b) * 0.9)/float(k)) - 100)
                sheet[row][1].value = float(b)
                sheet[row][2].value = float(k)
                sheet[row][3].value = raznica
                sheet[row][4].value = procent
                row += 1
    book.save("yasmart.xlsx")
    book.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
