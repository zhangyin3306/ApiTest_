import sys
sys.path.append(r"C:\ProgramData\Jenkins\.jenkins\workspace\ApiTest")
import os
import pytest,jsonpath,json,allure
from common.Base import excel_is_Y_run
from config import Conf
from config.Conf import ConfigYaml
from common.global_dict import GlobalDict
from utils.RequestUtil import RequestsUtil
from string import Template

case_info  = ConfigYaml().config
util = RequestsUtil()

html_path = Conf.get_report_path() + os.sep + "html"
report_result_path = Conf.get_report_path() + os.sep + "result"



class TestExcel_case:
    # @allure.title("维保通接口回归")
    # @allure.description("维保通平台接口回归,涵盖系统主要模块的正向流程,包括:运维工单.需求管理.")
    run_list = excel_is_Y_run()

    @pytest.mark.parametrize("case",run_list)
    def test_run_excel_case(self,case):
        """
        运用pytest参数化读取excel中的接口用例,
        执行封装后request判断method类型调用接口用例,
        解决接口依赖:提取接口响应内容存入字典,利用Template方法将字典内容与参数占位符替换
        :param case:
        :return:
        """

        url = case_info["url"] + case[case_info["excel"]["url"]]
        # headers = json.loads(case[case_info["excel"]["headers"]])
        method = case[case_info["excel"]["method"]]
        extract = case[case_info["excel"]["extract"]]
        extract2 = case[case_info["excel"]["extract2"]]
        json_data = case[case_info["excel"]["json_data"]]
        params = case[case_info["excel"]["params"]]
        case_id = case[case_info["excel"]["case_id"]]
        case_name = case[case_info["excel"]["case_name"]]
        dic = GlobalDict().show_dict()

        # 替换模板中的变量
        if "$" in json_data:
            try:
                json_data = Template(json_data).substitute(dic)
                print(f"传递json参数: {json_data}")  # 打印替换后的json_data以便调试
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
                raise

        if "$" in params:
            try:
                params = Template(params).substitute(dic)
                print(f"传递params参数：: {params}")
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")


        # 请求头默认了，所以不用重新赋值
        res = util.requests_api(url, method, json=json_data, params=params)
        print(res.json())

        #allure测试报告中的标题和描述
        allure.dynamic.title(f'{case_name +"-"+ case_id}')
        # allure.dynamic.description(f'{res.json()}')


        if extract:
            lst =jsonpath.jsonpath(res.json(),'$..'+extract)
            GlobalDict().set_dict(extract,lst[0])
            # print("存入字典的值："+GlobalDict().show_dict())
        if extract2:
            lst2 = jsonpath.jsonpath(res.json(), '$..' + extract2)
            GlobalDict().set_dict(extract2, lst2[0])







if __name__ == '__main__':
   # allure generate report/result -o ../report/html --clean
   pytest.main(['-s',"--alluredir",report_result_path])
   # report_html(report_result_path,html_path)
   # subprocess.call('allure open -h 127.0.0.1 -p 9999 ./report/html', shell=True)





