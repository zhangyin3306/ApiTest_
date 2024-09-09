from utils.ExcelUtlil import ExcelUtlil
reader = ExcelUtlil('../case/xx.xlsx')
res = reader.read_excel_as_dict()
run_list= []
for line in res:
    if line["是否运行"] == "Y":
        run_list.append(line)
print(len(run_list))
