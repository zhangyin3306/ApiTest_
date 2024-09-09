import requests
from requests.utils import unquote_header_value

from utils.EncryptUtil import Encrypt
from utils.CodeUtlil import ocr
from utils.LogUtil import my_log
from config.Conf import ConfigYaml

logger = my_log()
class Login:

    def __init__(self, username=None, password=None):
        self.config = ConfigYaml()
        self.logger = my_log()
        self.username = self.config.TestLogin["data"]["username"]
        self.password = self.config.TestLogin["data"]["password"]
        if username and password:
            self.username = self.config.TestLogin["data"]["username"]
            self.password = self.config.TestLogin["data"]["password"]
        self.base_url = "https://test-napi.bangdao-tech.com/charging-maintenance-server"
        self.captcha_url = self.base_url + "/captchaImage"
        self.login_url = self.base_url + "/login"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
        }
        self.session = requests.Session()

    def login_ll(self):
        self.username = self.config.TestLogin["data"]["username"]
        self.password = self.config.TestLogin["data"]["password"]
        print(self.password+"and "+self.username)

    def get_captcha_and_uuid(self):
        response = self.session.get(url=self.captcha_url, headers=self.headers)
        response_data = response.json()
        image = response_data['data']['image']
        uuid = response_data['data']['uuid']
        return image, uuid

    def login(self, max_attempts=3):
        attempts = 0
        while attempts < max_attempts:
            image, uuid = self.get_captcha_and_uuid()
            encrypted_username = Encrypt(self.username)
            encrypted_password = Encrypt(Encrypt(self.password))
            data = {
                "username": encrypted_username,
                "password": encrypted_password,
                "code": ocr(image),
                "uuid": uuid,
                "salt": "",
            }
            response = self.session.post(url=self.login_url, json=data, headers=self.headers)

            response_data = response.json()
            code = response_data.get('code')

            if code == "10000":
                # 登录成功，跳出循环
                return response_data
            else:
                attempts += 1
                logger.warning(f"登录尝试 {attempts} 失败。Code: {code}。重试...")
        # 如果达到最大尝试次数但登录仍然失败，记录错误消息
        logger.error(f"在 {max_attempts} 次尝试后登录失败。")
        return response_data  # 返回最后一次尝试获取的响应数据


if __name__ == '__main__':
    login = Login()
    print(login.login())