import allure
import requests

class TestOrderList:

    @allure.title('Позитивная проверка вывода списка заказов')
    def test_order_list_success(self):
        response = requests.get("https://qa-scooter.education-services.ru/api/v1/orders")
        r = response.json()

        assert response.status_code == 200
        assert r['orders']