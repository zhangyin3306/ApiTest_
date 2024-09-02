import os.path
import yaml


class YamlReader:
    # 判断文件是否存在
    def __init__(self,yaml_if):
        if os.path.exists(yaml_if):
            self.yaml_if=yaml_if
        else:
            raise FutureWarning("文件不存在！")
        self._data = None
        self._data_all = None
    def data(self):
        if not self._data:
           with open(self.yaml_if,'rb') as f:
               self._data = yaml.safe_load(f)
        return self._data
    def data_all(self):
        if not self._data_all:
           with open(self.yaml_if,'rb') as f:
               self._data_all = list(yaml.safe_load_all(f))
        return self._data_all

