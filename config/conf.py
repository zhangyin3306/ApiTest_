import os
from compileall import compile_file
from utils.YamlUtlil import YamlReader
# 1、获取当前项目的绝对路径
current = os.path.abspath(__file__)
base_dir = os.path.dirname(os.path.dirname(current))
# 定义config目录的路径
_config_path = base_dir+os.sep+"config"
# 定义conf.yaml路径
_config_file = _config_path+os.sep+ "conf.yaml"
def get_config_path():
    return _config_path

def get_config_file():
    return _config_file

# 2、读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
    def get_config_url(self):
        return self.config["BASE"]["test"]["url"]
if __name__ == '__main__':
    config  = ConfigYaml()
    print(config.get_config_url())