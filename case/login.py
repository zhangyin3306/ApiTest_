#登录
import os
import pytest
from Tools.scripts.generate_opcode_h import header

from config import Conf
from utils.YamlUtlil import YamlReader
from  config.Conf import ConfigYaml
import requests

# test_file = os.path.join(Conf.get_data_path(),"TestLogin.yaml")
# data_list = YamlReader(test_file).data_all()
from utils.RequestsUtil import RequestsUtil
# print(type(data_list))


#登录
login_yml = "TestLogin.yaml"
data_path = Conf.get_data_path()
filename = data_path+os.sep + login_yml
#print(filename)
def get_login_info():
    return YamlReader(filename).data_all()

print(get_login_info())
@pytest.mark.parametrize("login",get_login_info())
def test_1(login):
    url = login["url"]
    data = login["data"]
    res = requests.post(url=url,json=data)
    print(res)


if __name__ == "__main__":
    pytest.main(["-s","analysis_yaml_data.py"])




