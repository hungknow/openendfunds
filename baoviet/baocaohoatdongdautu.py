import pandas as pd

# Read the content of Excel file

def read_BaoCaoHoatDongDauTu(excelFilePath):
    excel_data_df = pd.read_excel(excelFilePath, index_col=0)
    print('Excel Sheet to JSON:', excel_data_df.to_json(orient='records'))
