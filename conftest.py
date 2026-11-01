import pytest
import requests
import api_methods
import urls
import api_requests


@pytest.fixture(scope="function")
def create_and_delete_courier(requests_object):
    user = api_methods.register_new_courier_and_return_login_password()
    yield user
    payload = {
        'login': user[0],
        'password': user[1]
    }
    response = requests_object.login_courier(payload)
    r = response.json()
    id_courier = r['id']
    requests_object.delete_courier(id_courier)

@pytest.fixture(scope="function")
def id_courier():
    id_courier = api_methods.return_id_after_login()
    yield id_courier

@pytest.fixture(scope="function")
def delete_courier():
    couriers_id = []
    def add_courier(login_courier, password):
        response = requests.post(urls.courier_login_url, data={"login": login_courier, "password": password})
        couriers_id.append(response.json()['id'])

    yield add_courier
    for ids in couriers_id:
        requests.delete(f'{urls.courier_delete_url}{ids}')

@pytest.fixture(scope="function")
def requests_object():
    return api_requests.RequestsApi()