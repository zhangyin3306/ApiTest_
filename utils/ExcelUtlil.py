import os
import pandas as pd


def read_excel_data():
    """
    读取excel为Y的用例
    :return:
    """
    reader = ExcelUtlil('../case/xx.xlsx')
    res = reader.read_excel_as_dict()
    run_list = []
    for line in res:
        if line["是否运行"] == "Y":
            run_list.append(line)
    print(len(run_list))


class ExcelUtlil:
    def __init__(self, file_path):
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            raise FileNotFoundError("文件不存在!!")

    def read_excel_as_dict(self, columns=None,sheet_name=0):
        """
        从 Excel 文件中读取指定列的数据，并以字典形式返回。
        参数:
        - file_path (str): Excel 文件的路径。
        - columns (list of str): 要读取的列名列表。如果为 None，则读取所有列。
        - sheet_name (int or str): 要读取的工作表名称或索引，默认为第一个工作表。
        - engine (str): 读取 Excel 文件所使用的引擎，默认为 'openpyxl'。
        返回:
        - dict: 包含指定列的数据的字典。
        """
        # 读取 Excel 文件
        df = pd.read_excel(self.file_path,sheet_name=sheet_name, engine='openpyxl')
        # 选择指定的列
        if columns is not None:
            df = df[columns]
        # orient='records' 将每一行转换为一个字典，并将所有行放入一个列表中
        result_dict = df.to_dict(orient='records')
        return result_dict

if __name__ == '__main__':
    # 示例使用
    file_path = '../case/xx.xlsx'
    columns_to_read = ['用例id', '模块']  # 读取 'Name' 列和 'Age' 列
    eu = ExcelUtlil(file_path)
    # 调用函数
    result = eu.read_excel_as_dict()
    # 输出结果
    print(result)
