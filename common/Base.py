#1、定义init_db
import datetime,os
from config import Conf
from utils.EmaillUtil import SendUtil
from utils.LogUtil import Logger
from utils.MysqlUtil import mysqlutil
from config.Conf import ConfigYaml

def init_db():
    """
    初始化测试库信息
    :param :
    :return:
    """
    db_info = ConfigYaml().get_conf_db()
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    #3、初始化mysql对象
    conn = mysqlutil(host,user,password,db_name)
    print(conn)
    return conn
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
    log_extension = ConfigYaml().get_conf_log_extension()
    logfile = os.path.join(log_path, current_time + log_extension)
    # print(logfile)
    # 日志文件级别
    loglevel = ConfigYaml().get_conf_log()
    return Logger(log_file=logfile,log_name=log_name,log_level=loglevel).logger

if __name__ == '__main__':
    # init_db()
    my_log().info("this is a debug message")