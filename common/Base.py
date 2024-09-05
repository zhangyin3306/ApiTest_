#1、定义init_db
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
if __name__ == '__main__':
    init_db("db_1")