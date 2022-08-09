import allure
import httpretty

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.requests_custom import CustomRequests


@allure.epic("Auth cases")
@httpretty.activate
class TestUserAuth(BaseCase):
    # def setup(self):
    #     data = {"name": "morpheus",
    #             "job": "leader"
    #             }
    #     response = CustomRequests.get("/user/login", data=data)
    #     self.auth_sid = self.get_cookie(response, "auth_sid")
    #     self.token = self.get_header(response, "x-csrf-token")
    #     self.user_id_from_auth_method = self.get_json_value(response, "user_id")

    @allure.description("Positive auth user")
    def test_auth_user(self):
        httpretty.enable(verbose=True, allow_net_connect=True)

        data = {"name": "morpheus",
                "job": "leader"
                }
        response = CustomRequests.get("api/users?page=2",
                                      data=None,
                                      headers=None,
                                      cookies=None)
        Assertions.assert_json_value_by_name(
            response,
            "name",
            "morpheus",
            "User id from auth method is not equal to user id from check method"
        )

        httpretty.disable()
        httpretty.reset()
