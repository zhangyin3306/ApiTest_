import pandas as pd

# 文件路径
file_path = 'xx.xlsx'

# 读取 Excel 文件
# 使用 'openpyxl' 引擎来处理 .xlsx 文件
df = pd.read_excel(file_path, engine='openpyxl')

# 查看 DataFrame 的前几行
print(df.head())

# 如果你想查看所有数据，可以使用
print(df)