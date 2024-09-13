import json
import sys
from time import perf_counter

import pytest
import self
from numpy.distutils.conv_template import header

from common.Base import excel_is_Y_run, my_log, get_case_list,get_case_pre
from config.Conf import ConfigYaml
from common import Base
from utils.RequestsUtil import RequestsUtil

case_file = ConfigYaml().config["case_file"]
sheet_by = ConfigYaml().config["sheet_by"]
run_list = excel_is_Y_run(case_file, sheet_by)

log = my_log()


class TestExcel_case:

    def run_api(self,url,method=None,headers=None,params=None):
        if str(method).lower() == "get":
            res = RequestsUtil().requests_api(url, 'get', headers, params)
        elif str(method).lower() == "post":
            res = RequestsUtil().requests_api(url, 'post', headers, params)
        else:
            log.error(f"请求类型错误.{method}")
        return res

    def run_pre(self,pre_case):
        url = ConfigYaml().config["url"] + pre_case[ConfigYaml().config["excel"]["url"]]
        method = pre_case[ConfigYaml().config["excel"]["method"]]
        params = pre_case[ConfigYaml().config["excel"]["params"]]
        headers = pre_case[ConfigYaml().config["excel"]["headers"]]
        cookies = pre_case[ConfigYaml().config["excel"]["cookies"]]
        if len(str(params).strip()) != 0:
            params = json.loads(params)
        if len(str(headers).strip()) != 0:
            headers = json.loads(headers)

        pre = self.run_api(url,method,headers,params)
        # print(f"前置用例执行{pre}")
        return pre


    @pytest.mark.parametrize("Case",run_list)
    def test_run_excel_case(self,Case):
        url = ConfigYaml().config["url"]+Case[ConfigYaml().config["excel"]["url"]]
        case_id=Case[ConfigYaml().config["excel"]["case_id"]]
        case_model=Case[ConfigYaml().config["excel"]["case_model"]]
        case_name=Case[ConfigYaml().config["excel"]["case_name"]]
        pre_exec=Case[ConfigYaml().config["excel"]["pre_exec"]]
        method=Case[ConfigYaml().config["excel"]["method"]]
        params_type=Case[ConfigYaml().config["excel"]["params_type"]]
        params=Case[ConfigYaml().config["excel"]["params"]]
        expect_result=Case[ConfigYaml().config["excel"]["expect_result"]]
        actual_result=Case[ConfigYaml().config["excel"]["actual_result"]]
        is_run=Case[ConfigYaml().config["excel"]["is_run"]]
        headers=Case[ConfigYaml().config["excel"]["headers"]]
        cookies= Case[ConfigYaml().config["excel"]["cookies"]]
        code=Case[ConfigYaml().config["excel"]["code"]]
        db_verify=Case[ConfigYaml().config["excel"]["db_verify"]]



        # # print(url,headers,params)
        # print(type(headers))
        # # 如果你想打印 headers 的内容来验证它是否正确设置
        # for key, value in headers.items():
        #     print(f"{key}: {value}")



        if  len(str(params).strip()) != 0:
            params  = json.loads(params)
        if  len(str(headers).strip()) != 0:
            headers  = json.loads(headers)

        # 验证前置条件,找到前置条件用例
        if pre_exec:
            pass
            pre_case  = get_case_pre(pre_exec)
            print(f"前置条件信息为{pre_exec}")
            per_res =  self.run_pre(pre_case)
            headers,cookies = self.get_correlation(headers,cookies,per_res)
        headers = json.loads(headers)
        pre = self.run_api(url, method, headers, params)
        print(f"用例执行{pre}")

    def get_correlation(self, headers, cookies, pre_res):
        """
        关联
        :param headers:
        :param cookies:
        :param pre_res:
        :return:
        """
        # 验证是否有关联
        headers_para, cookies_para = Base.params_find(headers, cookies)
        # 有关联，执行前置用例，获取结果
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
            # 结果替换
            headers = Base.res_sub(headers, headers_data)
        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
            # 结果替换
            cookies = Base.res_sub(headers, cookies_data)
        return headers, cookies



if __name__ == '__main__':
    pytest.main(["-s","test_excel_case.py"])


