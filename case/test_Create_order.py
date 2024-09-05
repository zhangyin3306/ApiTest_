from ctypes.wintypes import POINT

import pytest

from common.Base import init_db
from utils.RequestsUtil import RequestsUtil
from utils.AssertUtil import AssertUtil
from common import Base

def test_Create_order():
    requestsUtil = RequestsUtil()
    # 创建工单
    url = "https://test-napi.bangdao-tech.com/charging-maintenance-server/maintenance/orderNo?orderTypeId=453622917134237696"
    submit_url = "https://test-napi.bangdao-tech.com/charging-maintenance-server/maintenance/saveOrderInfo"
    headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEwMDAwLTM1MzkwZGNiLWM5ZTMtNDFkYS1hZGJmLWYwMmE2MmQ4YjA0NiJ9.'
                        'DjM4yAKdUxAE1feKkuiC6vpa8rFX-2VaSOiWpy-CuEsnMbn5Re5xBPeoh2HVCi_lHLaX1xQzF2PcQ4x9jJ6wTw'
    }
    response = requestsUtil.requests_api(url=url,method='get',headers=headers)
    AssertUtil().assert_code(response["code"],"200")

    # 数据库-断言
    # con = init_db("db_1")
    # res_db = con.fetchone("SELECT * FROM `cm_order_info` ")
    # print(res_db)
    # assert response["body"]["data"] == res_db["order_no"]

    # 提交工单
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
    "orderNo":response["body"]["data"],
    "handleUser": "10000",
    "handleUserName": "系统管理员"
    }
    response_submit = requestsUtil.requests_api(url=submit_url,method='post',headers=headers,json=data)
    AssertUtil().assert_code(response_submit["code"], "200")









if __name__ == '__main__':
    pytest.main("test_Create_order.py")