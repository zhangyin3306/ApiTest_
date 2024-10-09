import json

import requests
# import json
import logging


class RequestsUtil:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # excel表格中传递的字符串,需要它转化为字典进行传参.
        self.json=json.loads
    def requests_api(self, url, method, json=None, params=None,headers=None):
        """
        发送 HTTP 请求并返回响应对象。

        :param url: 请求的 URL
        :param method: 请求方法 (GET, POST, PUT, DELETE 等)
        :param json: JSON 数据 (可选)
        :param headers: 请求头 (可选)
        :param params: 查询参数 (可选)
        :return: requests.Response 对象
        """
        # 将 headers 从字符串转换为字典
        # if isinstance(headers, str):
        #     headers = json.loads(headers)
        # headers = headers or {}
        #

        method = method.lower()
        self.log.info(f"发送 {method.upper()} 请求到 {url}")

        try:
            if method == 'get':
                if type(params) != dict:
                    params = self.json(params)
                response = requests.get(url, headers=headers, params=params)
            elif method == 'post':
                if type(json) != dict:
                    json = self.json(json)
                response = requests.post(url, json=json,headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
        except requests.RequestException as e:
            self.log.error(f"请求失败: {e}")
            raise
        return response


# 使用示例
if __name__ == "__main__":
    util = RequestsUtil()

    url = 'https://test-napi.bangdao-tech.com/charging-maintenance-server/maintenance/orderNo'
    method = 'get'
    json_data = {}  # 用于 POST 请求的数据
    headers_str = '''
    {
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEwMDAwLTI0ODY1ODNhLWIyYzctNGEyMC05MzhlLTYzN2Q5NjY4OWJiNiJ9.NyqolDnLEBaujfEsRGvHgQSBqhwzCQcmHSe10K4c0wd1GO-OWCOvWjsZbsMIFRHmtj8wIXyxoYlVyHS9Cnk9-A",
        "orderTypeId": "453622917134237696"
    }
    '''
    headers = json.loads(headers_str)
    params = {"orderTypeId": "453622917134237696"}

    try:
        response = util.requests_api(url, method, json=json_data, headers=headers, params=params)
        code = response.status_code
        print(f"响应状态码: {code}")
        print(f"响应内容: {response.text}")
    except Exception as e:
        print(f"请求失败: {e}")