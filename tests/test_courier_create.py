import allure
import pytest
import data
import helpers


class TestCourierCreate:

    @allure.title('Позитивная проверка создания курьера с двумя вариантами заполнения полей')
    @pytest.mark.parametrize(
        'payload_field',
        [
            {
                "login": helpers.generate_random_strings(10),
                "password": helpers.generate_random_strings(10)
            },
            {
                "login": helpers.generate_random_strings(10),
                "password": helpers.generate_random_strings(10),
                "firstName": helpers.generate_random_strings(10)
            }
        ])
    def test_courier_create_success(self, payload_field, delete_courier, requests_object):
        payload = payload_field
        response = requests_object.create_courier(payload)

        assert response.status_code == 201
        assert response.text == '{"ok":true}'

        delete_courier(payload["login"], payload["password"])

    @allure.title('Негативная проверка регистрациции курьера с уже зарегистрированными данными')
    def test_register_existing_courier(self, requests_object):
        payload = {
                "login": helpers.generate_random_strings(10),
                "password": helpers.generate_random_strings(10),
                "firstName": helpers.generate_random_strings(10)
            }
        requests_object.create_courier(payload)
        response = requests_object.create_courier(payload)
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
    def test_register_new_courier_failure(self, payload_field, requests_object):
        payload = payload_field
        response = requests_object.create_courier(payload)
        r = response.json()

        assert response.status_code == 400
        assert r['message'] == data.register_not_all_fields_message
