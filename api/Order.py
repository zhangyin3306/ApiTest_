from api.login import Login
from utils.AssertUtil import AssertUtil
from utils.RequestUtil import RequestsUtil
from config.Conf import ConfigYaml
from login import Login



class Order:
    def __init__(self):
        self.login  = Login()
        self.conf = ConfigYaml()
        self.request_util = RequestsUtil()
        # 创建工单
        self.url = self.conf.config["url"]
        self.headers = {
           "Authorization" : "Bearer "+self.login.login()["data"]
        }
        print(self.headers)
        self.headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEwMDAwLTM1MzkwZGNiLWM5ZTMtNDFkYS1hZGJmLWYwMmE2MmQ4YjA0NiJ9.'
                             'DjM4yAKdUxAE1feKkuiC6vpa8rFX-2VaSOiWpy-CuEsnMbn5Re5xBPeoh2HVCi_lHLaX1xQzF2PcQ4x9jJ6wTw'
        }
    def Create(self,orderTypeId):
        """
        这个是工单创建接口。。。
        :param orderTypeId: 工单id必传
        :return: 返回响应结果
        """
        params = {
            "orderTypeId":orderTypeId
        }
        create = self.url + "/maintenance/orderNo"
        response = self.request_util.requests_api(url=create, method='get', headers=self.headers,params = params )
        AssertUtil().assert_code(response.status_code, "200")
        return response
    def Submit(self,orderNo):
        """
        提交工单，需要创建工单的编号
        :param orderNo:
        :return:
        """
        data = {
            "orderTypeParentId": "453622917134237696",
            "orderTypeId": "",
            "threeOrderTypeId": "",
            "urgencyLevel": "1",
            "orderDesc": "<p>对地点</p>",
            "stationName": "桩企测试专用站",
            "region": [
                "13",
                "1310",
                "131082"
            ],
            "address": "燕郊站",
            "checkGroupIds": [],
            "deviceNo": "",
            "deviceTypeName": "",
            "deviceModelName": "",
            "customerName": "",
            "contact": "",
            "contactTel": "",
            "carBrand": "",
            "carModel": "",
            "appointmentTime": "",
            "shelfLife": "0",
            "installMethod": "",
            "mainUser": "",
            "platform": "",
            "projectType": "",
            "projectCode": "",
            "installUnit": "",
            "enableMethod": "",
            "salesmanName": "",
            "businessType": "1",
            "businessTypeName": "充电",
            "city": "1310",
            "county": "131082",
            "deptName": "江南水务",
            "onlineDate": "2024-06-25",
            "operationMode": "1",
            "province": "13",
            "regionName": "江南水务",
            "stationAddress": "燕郊站",
            "stationCode": "zhang",
            "stationId": "463385701627645952",
            "status": "02",
            "orderNo": orderNo,
            "handleUser": "10000",
            "handleUserName": "系统管理员"
        }
        submit_address = self.url+"/maintenance/saveOrderInfo"
        response_submit = self.request_util.requests_api(url=submit_address, method='post', headers=self.headers, json=data)
        AssertUtil().assert_code(response_submit.status_code, "200")
        return response_submit


if __name__ == '__main__':
    Order_c  = Order()
    Order_c_s  =Order_c.Create("453622917134237696")
    print(Order_c.Create("453622917134237696"))
    # Order_submit = Order_c.Submit(Order_c_s["body"]["data"])
    # print(Order_submit)






