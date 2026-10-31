import allure
import requests


class TestDeleteCourier:

    @allure.title('Позитивная проверка удаления курьера')
    def test_delete_courier_success(self, id_courier):
        response = requests.delete(f"https://qa-scooter.education-services.ru/api/v1/courier/{id_courier}")

        assert response.status_code == 200
        assert response.text == '{"ok":true}'

    @allure.title('Негативная проверка логина курьера, запрос без id')
    def test_delete_courier_without_id(self):
        response = requests.delete("https://qa-scooter.education-services.ru/api/v1/courier")
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == 'Not Found.'

    @allure.title('Негативная проверка логина курьера, невалидный id')
    def test_delete_courier_invalid_id(self):
        id_courier = '33333'
        response = requests.delete(f"https://qa-scooter.education-services.ru/api/v1/courier/{id_courier}")
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == 'Курьера с таким id нет.'