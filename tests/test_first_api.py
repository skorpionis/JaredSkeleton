import requests
from httpretty import HTTPretty
from httpretty.core import HTTPrettyRequest
from lib.assertions import Assertions
from lib.base_case import BaseCase
import allure


@allure.epic("Auth cases")
class TestUserAuth(BaseCase):
    def setup(self):
        data = {'email': 'sdsd@mail.ru',
                'password': '1234'
                }
        response = requests.get("URL", data=data)
        self.auth_sid = self.get_cookie(response, "auth_sid")
        self.token = self.get_header(response, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response, "user_id")

    @allure.description("Positive auth user")
    def test_auth_user(self):
        response = requests.get("URL",
                                headers={"x-csrf-token": self.token},
                                cookies={"auth_sid": self.auth_sid}
                                )
        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )
