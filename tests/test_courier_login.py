import allure
import pytest
import api_methods
import data


class TestCourierLogin:

    @allure.title('Позитивная проверка логина курьера')
    def test_login_success(self, create_and_delete_courier, requests_object):
        payload = {
            'login': create_and_delete_courier[0],
            'password': create_and_delete_courier[1]
        }
        response = requests_object.login_courier(payload)
        r = response.json()

        assert response.status_code == 200
        assert r['id']

    @allure.title('Негативная проверка логина курьера с отсутствием данных в полях')
    @pytest.mark.parametrize("creds_login",
                             [
                                 {'login': api_methods.register_new_courier_and_return_login_password()[0], 'password': ''},
                                 {'login': '', 'password': api_methods.register_new_courier_and_return_login_password()[1]}
                             ])
    def test_login_failure(self, creds_login, requests_object):
        payload = creds_login
        response = requests_object.login_courier(payload)
        r = response.json()

        assert response.status_code == 400
        assert r['message'] == data.login_not_all_fields_message

    @allure.title('Негативная проверка логина курьера с невалидными данными')
    @pytest.mark.parametrize("creds_login",
                             [
                                 {'login': api_methods.register_new_courier_and_return_login_password()[0], 'password': 'fjsdfkjgs'},
                                 {'login': 'oisdfoisdff', 'password': api_methods.register_new_courier_and_return_login_password()[1]}
                             ])
    def test_login_incorrect_field(self, creds_login, requests_object):
        payload = creds_login
        response = requests_object.login_courier(payload)
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == data.login_invalid_data_message