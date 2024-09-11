#1、定义init_db
from utils.EmaillUtil import SendUtil
from utils.MysqlUtil import mysqlutil
from config.Conf import ConfigYaml

def init_db(db_alias):
    #2、初始数据化信息，通过配置
    db_info = ConfigYaml().get_conf_db(db_alias)
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
    发送测试报告
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
if __name__ == '__main__':
    init_db("db_1")