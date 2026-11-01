import allure
import requests
import data
import urls


class TestDeleteCourier:

    @allure.title('Позитивная проверка удаления курьера')
    def test_delete_courier_success(self, id_courier):
        response = requests.delete(f"{urls.courier_delete_url}{id_courier}")

        assert response.status_code == 200
        assert response.text == '{"ok":true}'

    @allure.title('Негативная проверка удаления курьера, запрос без id')
    def test_delete_courier_without_id(self):
        response = requests.delete(urls.courier_delete_url)
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == data.delete_courier_without_id_message

    @allure.title('Негативная проверка удаления курьера, невалидный id')
    def test_delete_courier_invalid_id(self):
        id_courier = '33333'
        response = requests.delete(f"{urls.courier_delete_url}{id_courier}")
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == data.delete_courier_invalid_id_message