import requests


class creation_work_orders:
    def __init__(self):
        self.Creation_Work_orders_url = "https://test-napi.bangdao-tech.com/charging-maintenance-server/maintenance" \
                                        "/orderNo?orderTypeId=453622917134237696"
        self.Submit_Work_orders_url = "https://test-napi.bangdao-tech.com/charging-maintenance-server/maintenance" \
                                      "/saveOrderInfo"

    def Creation_of_Work_orders(self, headers):
        return requests.get(url=self.Creation_Work_orders_url, headers=headers)

    def Submit_Work_orders(self, data_2, headers):
        return requests.post(url=self.Submit_Work_orders_url, json=data_2, headers=headers)
