import datetime,os
import subprocess
import re

import pytest

from config import Conf
from config.Conf import ConfigYaml
from utils.EmaillUtil import SendUtil
from utils.Excelutil import ExcelReader
from utils.LogUtil import Logger

# 下面两个方法都用到这个对象，放在外面实例化
conf = ConfigYaml()
conf_path = conf.config




def send_email(report_html_path="",content="",title="测试"):
    """
    发送测试报告-邮件
    :param report_html_path: 测试报告
    :param content:
    :param title:
    :return:
    """
    email_info = ConfigYaml().get_conf_email()
    smtp_addr = email_info['smtpserver']
    username = email_info['username']
    password = email_info['password']
    recv = email_info['receiver']
    email = SendUtil(
        smtp_addr = smtp_addr,
        username =username,
        password =password,
        recv=recv,
        title = title,
        content=content,
        file = report_html_path
        )
    email.send()
def my_log(log_name = __file__):
    # 1、初始化参数数据
    # 日志文件名称，日志文件级别
    # 日志文件名称 = logs目录 + 当前时间+扩展名
    # log目录
    log_path = Conf.get_log_path()
    # 当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    # 扩展名
    log_extension = conf_path["BASE"]["log_extension"]
    logfile = os.path.join(log_path, current_time + log_extension)
    # print(logfile)
    # 日志文件级别
    loglevel = conf_path["BASE"]["log_lever"]
    return Logger(log_file=logfile,log_name=log_name,log_level=loglevel).logger



def excel_is_Y_run():
    # 这里需要写绝对路径,否则Jenkins读取不到
    absolute_path = os.path.abspath(conf_path["case_file"])
    reader = ExcelReader(absolute_path, conf_path["sheet_by"])
    run_list = []
    for line in reader.data():
        if line[conf_path["excel"]['is_run']] == "Y":
            run_list.append(line)
    return run_list


def report_html(report_result,report_html):
    report_path = f'allure generate {report_result} -o {report_html} --clean'
    subprocess.call(report_path, shell=True)












