import pytest
import requests

import helpers


@pytest.fixture(scope="function")
def create_courier():
    user = helpers.register_new_courier_and_return_login_password()
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
    id_courier = helpers.return_id_after_login()
    yield id_courier

@pytest.fixture(scope="function")
def delete_courier():
    yield
