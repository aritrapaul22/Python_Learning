import pandas, gspread, re, statistics


def getPublicSpreadsheet():
    # Accessing a Public Spreadsheet
    url = "https://docs.google.com/spreadsheets/d/1XKZw11Oodr6Ha3yZfUmei127XjuskpjKzwhJTG1Yl3A/gviz/tq?tqx=out:csv&sheet=DP"
    data = pandas.read_csv(url)
    print(data)

def getPrivateSpreadsheet():
    # Establish Connection
    # gc = gspread.service_account('udemypy-secrets.json')

    # Get Spreadsheet
    spreadsheet = gc.open('TestData_PyLearning')

    # Get Worksheet
    # worksheet = spreadsheet.get_worksheet(0)
    worksheet = spreadsheet.worksheet('Sheet1')

    # Get Cell
    data = worksheet.get_all_records()
    # row = worksheet.get_values('A5:F7')  # Get Row(s)
    row = worksheet.row_values(1)
    column = worksheet.col_values(2)[1:]

    # Get Cell using acell
    cell = worksheet.acell('D12').value

    # Search for a cell
    cellSearch= worksheet.find('1032')
    cells = worksheet.findall('10')
    # print(cells)

    # Search for partial matches
    reg = re.compile(r'10')
    regSearch = worksheet.findall(reg)

    for item in regSearch:
        print(item.row, item.col)

def updateCell():
    # Establish Connection
    # gc = gspread.service_account('udemypy-secrets.json')

    # Get Spreadsheet
    spreadsheet = gc.open('TestData_PyLearning')

    # Get Worksheet
    worksheet = spreadsheet.worksheet('Sheet1')

    # Update  a cell
    # worksheet.update([[22]], 'D5')

    # Update a cell based on row-column
    worksheet.update_cell(2,6,2000)

def updateColumn():
    # Establish Connection
    # gc = gspread.service_account('udemypy-secrets.json')

    # Get Spreadsheet
    spreadsheet = gc.open('TestData_PyLearning')

    # Get Worksheet
    worksheet = spreadsheet.worksheet('Sheet1')

    # Add a New Column
    tempCel = worksheet.get_values('E2:E26')
    tempFar = [[round((float(i[0]) * 9 / 5 + 32), 1)] for i in tempCel]

    worksheet.update([['Temp(F)']] + tempFar, 'G1:G26')

def calculateMean():
    # Establish Connection
    # gc = gspread.service_account('udemypy-secrets.json')

    # Get Spreadsheet
    spreadsheet = gc.open('TestData_PyLearning')

    # Get Worksheet
    worksheet = spreadsheet.worksheet('Sheet1')

    # Get Values
    tempFar = worksheet.get_values('G2:G26')
    tempFar = [float(i[0]) for i in tempFar]

    worksheet.update([[statistics.mean(tempFar)]], 'G27')

if __name__ == '__main__':
    calculateMean()
