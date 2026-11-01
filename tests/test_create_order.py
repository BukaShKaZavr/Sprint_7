import allure
import pytest
import data
import json


class TestCreateOrder:

    @allure.title('Позитивная проверка создания заказа')
    @pytest.mark.parametrize("order_data", [data.black_colour_order, data.gray_colour_order, data.both_colours_order, data.no_colour_order])
    def test_create_order_success(self, order_data, requests_object):

        payload = json.dumps(order_data)
        response = requests_object.create_order(payload)
        r = response.json()

        assert response.status_code == 201
        assert r['track']
