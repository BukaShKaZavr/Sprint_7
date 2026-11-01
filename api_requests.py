import requests
import urls

class RequestsApi:

    def create_courier(self, payload):
        return requests.post(urls.courier_create_url, payload)

    def login_courier(self, payload):
        return requests.post(urls.courier_login_url, payload)

    def delete_courier(self, id_courier=''):
        return requests.delete(f"{urls.courier_delete_url}{id_courier}")

    def create_order(self, payload):
        return requests.post(urls.order_create_url, payload)

    def order_list(self):
        return requests.get(urls.orders_list_url)