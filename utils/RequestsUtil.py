import requests

from utils.LogUtil import my_log



class RequestsUtil:
    def __init__(self):
        self.log = my_log()

    def requests_api(self,url,method,json=None,headers=None):
        if method == 'get':
            self.log.info("发送get请求")
            r = requests.get(url, headers=headers)
        elif method == 'post':
            self.log.info("发送post请求")
            r = requests.post(url,json= json,headers=headers)

        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res['code'] = code
        res['body'] = body
        return res

    def get(self,url,**kwargs):
        return self.requests_api(url,method='get',**kwargs)
    def post(self,url,**kwargs):
        return self.requests_api(url,method='post',**kwargs)