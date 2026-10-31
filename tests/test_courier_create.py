import allure
import pytest
import requests
import helpers

class TestCourierCreate:

    @allure.title('Позитивная проверка создания курьера с двумя вариантами заполнения полей')
    @pytest.mark.parametrize(
        'payload_field',
        [
        helpers.creds_for_register_all_fields(),
        helpers.creds_for_register_only_required_fields()
        ])
    def test_courier_create_success(self, payload_field):
        payload = payload_field
        response = requests.post('https://qa-scooter.education-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 201
        assert response.text == '{"ok":true}'

    @allure.title('Негативная проверка регистрациции курьера с уже зарегистрированными дпнными')
    def test_register_existing_courier(self):
        payload = helpers.creds_for_register_all_fields()
        requests.post('https://qa-scooter.education-services.ru/api/v1/courier', data=payload)
        response = requests.post('https://qa-scooter.education-services.ru/api/v1/courier', data=payload)
        r = response.json()

        assert response.status_code == 409
        assert r['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Негативная проверка регистрации курьера с неполными обязательными данными')
    @pytest.mark.parametrize(
        'payload_field',
        [
        {"login": "zdpbmfpewa", "password": "", "firstName": "xvwyinbfvl"},
        {"login": "", "password": "svbhvowrsp", "firstName": "xvwyinbfvl"}
        ])
    def test_register_new_courier_failure(self, payload_field):
        payload = payload_field
        response = requests.post('https://qa-scooter.education-services.ru/api/v1/courier', data=payload)
        r = response.json()

        assert response.status_code == 400
        assert r['message'] == 'Недостаточно данных для создания учетной записи'
