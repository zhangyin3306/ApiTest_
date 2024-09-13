import datetime,os
import re

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



def excel_is_Y_run(file=conf_path["case_file"],sheet_by=conf_path["sheet_by"]):
    reader = ExcelReader(file, sheet_by)
    run_list = []
    for line in reader.data():
        if line[conf_path["excel"]['is_run']] == "Y":
            run_list.append(line)
    return run_list
def get_case_list(file=conf_path["case_file"],sheet_by=conf_path["sheet_by"]):
    reader = ExcelReader(file, sheet_by)
    run_list = []
    for line in reader.data():
            run_list.append(line)
    return run_list

def get_case_pre(pre):
    """
    根据前置条件,从全部测试用例,找到对应的测试用例
    :param pre:
    :return:
    """
    run_list = get_case_list()
    for line in run_list:
        if pre in dict(line).values():
            return line
    return None
def res_find(data,pattern_data='\${(.*)}\$'):
    """
    查询
    :param data:
    :param pattern_data:
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res
def res_sub(data,replace,pattern_data='\${(.*)}\$'):
    """
    替换
    :param data:
    :param replace:
    :param pattern_data:
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        return re.sub(pattern,replace,data)
    return replace

def params_find(headers,cookies):
    """
    验证请求中是否有${}$需要结果关联的
    :param headers:
    :param cookie:
    :return:
    """
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_sub(cookies)
    return headers,cookies


if __name__ == '__main__':
    # print(my_log().info("这是一个日志"))
    print(res_find('{"Author":"jwt ${token}$"}'))
    print(res_sub('{"Author":"jwt ${token}$"}',"123"))
