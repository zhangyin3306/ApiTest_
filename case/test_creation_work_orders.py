# -*-coding：utf-8 -*-
from api.Creation_work_orders import creation_work_orders
import unittest


class Test_Creation_work_order(unittest.TestCase):
    def setUp(self) -> None:
        self.creation_work_orders = creation_work_orders()

    def test_Creation_work_order(self):
        # 创建工单
        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEwMDAwLTYwZjU2YmIwLTRhYzItNGU0OS1iOTVkLWQ4YTgyNGY0ZThjNCJ9.'
                             'VbBvAeW1DnTzqE0vqthBg2586MGKzzrEW864xKkjkk3hXm6YEFd225nPxwMFQ-S5LBqS9RTZAtpIMyr9bfn0Fw'
        }
        v1 = self.creation_work_orders.Creation_of_Work_orders(headers=headers)
        print(v1.json()['data'])

        # 提交工单
        data_2 = {
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
            "orderNo": v1.json()['data'],
            "handleUser": "10000",
            "handleUserName": "系统管理员"
        }

        v2 = self.creation_work_orders.Submit_Work_orders(data_2=data_2, headers=headers)
        print(v2.request.body)
        print(v2.status_code)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    Test_Creation_work_order()
