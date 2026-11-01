import allure
import data


class TestDeleteCourier:

    @allure.title('Позитивная проверка удаления курьера')
    def test_delete_courier_success(self, id_courier, requests_object):
        response = requests_object.delete_courier(id_courier)

        assert response.status_code == 200
        assert response.text == '{"ok":true}'

    @allure.title('Негативная проверка удаления курьера, запрос без id')
    def test_delete_courier_without_id(self, requests_object):
        response = requests_object.delete_courier()
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == data.delete_courier_without_id_message

    @allure.title('Негативная проверка удаления курьера, невалидный id')
    def test_delete_courier_invalid_id(self, requests_object):
        id_courier = '33333'
        response = requests_object.delete_courier(id_courier)
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == data.delete_courier_invalid_id_message