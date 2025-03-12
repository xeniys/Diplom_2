import allure
import pytest

from functions.auth_api import AuthResponses
from helper import UserData
from constants import Messages


class TestUserLogin:
    @allure.title('Логин пользователя: логин под существующим пользователем')
    def test_user_login(self):
        user_body = UserData.generate_fake_user_data()
        user = AuthResponses.create_user(user_body)
        login = AuthResponses.user_login(user_body)

        AuthResponses.delete_user(user)

        assert login.status_code == 200 and 'accessToken' in login.json()

    @allure.title('Логин пользователя: логин с неверным логином и паролем')
    @pytest.mark.parametrize('field',
                             [
                                 pytest.param('email', id='тест с email'),
                                 pytest.param('password', id='тест с password')
                             ]
                             )
    def test_user_login_with_wrong_params(self, field):
        user_body = UserData.generate_fake_user_data()
        user = AuthResponses.create_user(user_body)
        user_body_v2 = user_body.copy()
        user_body_v2[field] = user_body[field] + 'SOMETHING_WRONG'
        login = AuthResponses.user_login(user_body_v2)

        AuthResponses.delete_user(user)

        assert login.status_code == 401 and login.json()['message'] == Messages.INCORRECT_DATA
