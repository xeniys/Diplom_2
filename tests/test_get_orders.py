import allure

from functions.auth_api import AuthResponses
from functions.orders_api import OrdersResponse
from helper import UserData
from constants import Messages
from data import Data


class TestGetOrders:
    @allure.title('Получение заказов конкретного пользователя: с авторизацией')
    def test_get_user_orders(self):
        user_body = UserData.generate_fake_user_data()
        user = AuthResponses.create_user(user_body)
        OrdersResponse.create_order(user, Data.ingredients)
        orders_list = OrdersResponse.get_orders(user)

        AuthResponses.delete_user(user)

        assert orders_list.status_code == 200 and 'orders' in orders_list.json()

    @allure.title('Получение заказов конкретного пользователя: без авторизации')
    def test_get_user_orders_without_auth(self):
        orders_list = OrdersResponse.get_orders_without_auth()

        assert orders_list.status_code == 401 and orders_list.json()['message'] == Messages.WITHOUT_AUTH
