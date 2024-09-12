import xlrd
import os



class ExcelReader:
    """
    需要传文件地址、sheet页
    """
    def __init__(self, excel_file,sheet_by):
        if os.path.exists(excel_file):
            self.file = excel_file
            self.sheet_by = sheet_by
            self._data =[]
        else:
            raise FileNotFoundError("文件不存在")

    def data(self):
        if not self._data:
            if type(self.sheet_by) == int:
                workbook = xlrd.open_workbook(self.file)
                worksheet = workbook.sheet_by_index(self.sheet_by)
            else:
                raise TypeError("需要输入整数,我才能知道是那一页")
            title = worksheet.row_values(0)
            for col in range(1,worksheet.nrows):
                col_value = worksheet.row_values(col)
                self._data.append(dict(zip(title,col_value)))

        return self._data


if __name__ == '__main__':
    reader = ExcelReader("../data/test.xlsx",0)
    print(reader.data())
