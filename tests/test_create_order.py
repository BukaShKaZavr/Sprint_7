import allure
import pytest
import requests
import data
import json

import urls


class TestCreateOrder:

    @allure.title('Позитивная проверка создания заказа')
    @pytest.mark.parametrize("order_data", [data.black_colour_order, data.gray_colour_order, data.both_colours_order, data.no_colour_order])
    def test_create_order_success(self, order_data):

        payload = json.dumps(order_data)
        response = requests.post(urls.order_create_url, data=payload)
        r = response.json()

        assert response.status_code == 201
        assert r['track']
