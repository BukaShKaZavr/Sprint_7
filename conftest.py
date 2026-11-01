import pytest
import requests
import api_methods
import urls


@pytest.fixture(scope="function")
def create_courier():
    user = api_methods.register_new_courier_and_return_login_password()
    yield user
    payload = {
        'login': user[0],
        'password': user[1]
    }
    response = requests.post("https://qa-scooter.education-services.ru/api/v1/courier/login", data=payload)
    r = response.json()
    id_courier = r['id']
    requests.delete(f"https://qa-scooter.education-services.ru/api/v1/courier/{id_courier}")

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