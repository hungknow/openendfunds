import pandas as pd
import datetime

class BaoVietBaoCaoHoatDongDauTu:
    def __init__(self, fromDate, toDate):
        self.fromDate = fromDate
        self.toDate = toDate

# Read the content of Excel file

def read_BaoCaoHoatDongDauTu(excelFilePath):
    excel_data_df = pd.read_excel(excelFilePath, sheet_name=None, header=None)
    firstSheet = excel_data_df['Tong quat']
    fromDate = datetime.date(firstSheet[3][4], firstSheet[3][3], 1)
    toDate = datetime.date(firstSheet[3][4], firstSheet[3][3], 31)
    # print(fromDate)

    # print('Excel Sheet to JSON:', excel_data_df.to_json(orient='records'))
    return firstSheet
