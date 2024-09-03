import requests
from utils.RequestsUtil import RequestsUtil


def Create_order():
    requestsUtil = RequestsUtil()
    # 创建工单
    url = "https://test-napi.bangdao-tech.com/charging-maintenance-server/maintenance/orderNo?orderTypeId=453622917134237696"
    submit_url = "https://test-napi.bangdao-tech.com/charging-maintenance-server/maintenance/saveOrderInfo"
    headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEwMDAwLWU3YjZlOGU4LWY5NmQtNGMyZS05ZjU3LTM3Yzk1YWJjNGVhNSJ9.0yNLEltGYz0f1jAlj0K_dqrOtWtBwu3ogL17ZAtHpxd-pV5vJ6EN3tq6NxvXgpwGgj18WHm3WwkdT0E7HhYwsg'
    }
    response = requestsUtil.requests_api(url=url,method='get',headers=headers)
    print(response)
    print(response["body"]["data"])
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
    print(response_submit)
if __name__ == '__main__':
    Create_order()
