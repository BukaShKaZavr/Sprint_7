import allure
import pytest
import requests
import data
import helpers
import urls


class TestCourierCreate:

    @allure.title('Позитивная проверка создания курьера с двумя вариантами заполнения полей')
    @pytest.mark.parametrize(
        'payload_field',
        [
            {
                "login": helpers.generate_random_string(10),
                "password": helpers.generate_random_string(10)
            },
            {
                "login": helpers.generate_random_string(10),
                "password": helpers.generate_random_string(10),
                "firstName": helpers.generate_random_string(10)
            }
        ])
    def test_courier_create_success(self, payload_field, delete_courier):
        payload = payload_field
        response = requests.post(urls.courier_create_url, data=payload)

        assert response.status_code == 201
        assert response.text == '{"ok":true}'

        delete_courier(payload["login"], payload["password"])

    @allure.title('Негативная проверка регистрациции курьера с уже зарегистрированными данными')
    def test_register_existing_courier(self):
        payload = {
                "login": helpers.generate_random_string(10),
                "password": helpers.generate_random_string(10),
                "firstName": helpers.generate_random_string(10)
            }
        requests.post(urls.courier_create_url, data=payload)
        response = requests.post(urls.courier_create_url, data=payload)
        r = response.json()

        assert response.status_code == 409
        assert r['message'] == data.register_existing_courier_message

    @allure.title('Негативная проверка регистрации курьера с неполными обязательными данными')
    @pytest.mark.parametrize(
        'payload_field',
        [
        {"login": "zdpbmfpewa", "password": "", "firstName": "xvwyinbfvl"},
        {"login": "", "password": "svbhvowrsp", "firstName": "xvwyinbfvl"}
        ])
    def test_register_new_courier_failure(self, payload_field):
        payload = payload_field
        response = requests.post(urls.courier_create_url, data=payload)
        r = response.json()

        assert response.status_code == 400
        assert r['message'] == data.register_not_all_fields_message
