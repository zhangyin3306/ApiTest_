import sys
sys.path.append("..")
import subprocess
from common.Base import report_html, send_email
import os
import pytest
from config import Conf



html_path = Conf.get_report_path() + os.sep + "html"
report_result_path = Conf.get_report_path() + os.sep + "result"



if __name__ == '__main__':
   # allure generate report/result -o ../report/html --clean
   pytest.main(['-s',"--alluredir",report_result_path])
   report_html(report_result_path,html_path)
   send_email(title="测试报告结果",content=html_path)
   # subprocess.call('allure open -h 127.0.0.1 -p 9999 ./report/html', shell=True)