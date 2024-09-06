import os
from compileall import compile_file
from utils.YamlUtlil import YamlReader
# 1、获取当前项目的绝对路径
current = os.path.abspath(__file__)
base_dir =os.path.dirname(os.path.dirname(current))

# 定义config目录的路径
_config_path = base_dir+os.sep+"config"

# 定义config目录的路径
_config_data_path = base_dir+os.sep+"data"

# 定义conf.yaml路径
_config_file = _config_path+os.sep+ "conf.yaml"
# 定义日志路径
_log_path = base_dir +os.sep+ "logs"
# 定义mysql路径
_db_config_file = _config_path+os.sep+ "db_sql.yaml"


def get_config_path():
    return _config_path
def get_data_path():
    return _config_data_path

def get_config_file():
    return _config_file

def get_log_path():
    return _log_path

def db_config_file():
    return _db_config_file


# 2、读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_sql = YamlReader(db_config_file()).data()
        # self.TestLogin = YamlReader(get_login_path()).data()
    def get_config_url(self):
        return self.config["BASE"]["test"]["url"]
    def get_conf_log(self):
        return self.config["BASE"]["log_lever"]
    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]
    def get_conf_db(self,db_host):
        return self.db_sql[db_host]
    # def get_conf_login_path(self,data):
    #     return self.TestLogin[data]
if __name__ == '__main__':
    config  = ConfigYaml()
    # print(config.get_config_url())
    # print(config.get_conf_log())
    # print(config.get_conf_log_extension())
    # print(config.get_conf_db("db_1"))
    print(config.get_conf_login_path("test"))
