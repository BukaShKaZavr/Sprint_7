import allure


class TestOrderList:

    @allure.title('Позитивная проверка вывода списка заказов')
    def test_order_list_success(self, requests_object):
        response = requests_object.order_list()
        r = response.json()

        assert response.status_code == 200
        assert r['orders']