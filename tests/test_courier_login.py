import allure
import pytest
import requests
import helpers

class TestCourierLogin:

    @allure.title('Позитивная проверка логина курьера')
    def test_login_success(self, create_courier):
        payload = {
            'login': create_courier[0],
            'password': create_courier[1]
        }
        response = requests.post("https://qa-scooter.education-services.ru/api/v1/courier/login", data=payload)
        r = response.json()

        assert response.status_code == 200
        assert r['id']

    @allure.title('Негативная проверка логина курьера с отсутствем данных в полях')
    @pytest.mark.parametrize("creds_login",
                             [
                                 {'login': helpers.register_new_courier_and_return_login_password()[0], 'password': ''},
                                 {'login': '', 'password': helpers.register_new_courier_and_return_login_password()[1]}
                             ])
    def test_login_failure(self, creds_login):
        payload = creds_login
        response = requests.post("https://qa-scooter.education-services.ru/api/v1/courier/login", data=payload)
        r = response.json()

        assert response.status_code == 400
        assert r['message'] == 'Недостаточно данных для входа'

    @allure.title('Негативная проверка логина курьера с невалидными данными')
    @pytest.mark.parametrize("creds_login",
                             [
                                 {'login': helpers.register_new_courier_and_return_login_password()[0], 'password': 'fjsdfkjgs'},
                                 {'login': 'oisdfoisdff', 'password': helpers.register_new_courier_and_return_login_password()[1]}
                             ])
    def test_login_incorrect_field(self, creds_login):
        payload = creds_login
        response = requests.post("https://qa-scooter.education-services.ru/api/v1/courier/login", data=payload)
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == 'Учетная запись не найдена'