import allure
import requests
import urls


class TestOrderList:

    @allure.title('Позитивная проверка вывода списка заказов')
    def test_order_list_success(self):
        response = requests.get(urls.orders_list_url)
        r = response.json()

        assert response.status_code == 200
        assert r['orders']