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




def get_config_path():
    return _config_path
def get_data_path():
    return _config_data_path

def get_config_file():
    return _config_file

def get_log_path():
    return _log_path




# 2、读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
    def get_config_url(self):
        return self.config["BASE"]["test"]["url"]
    # def get_conf_log(self):
    #     return self.config["BASE"]["log_lever"]
    # def get_conf_log_extension(self):
    #     return self.config["BASE"]["log_extension"]
    def get_conf_email(self):
        return self.config["email"]

    def get_conf_db(self):
        return self.config["db_1"]





if __name__ == '__main__':
    data = ConfigYaml()
    print(data.config["excel"])

