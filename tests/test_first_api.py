import json

import allure
import httpretty
import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.requests_custom import CustomRequests
from util.harness import Util


@allure.epic("Auth cases")
@httpretty.activate
class TestUserAuth(BaseCase):

    @httpretty.activate(allow_net_connect=False)
    def test_new(self):
        read_body = Util.read_json_from_file('data.json')
        httpretty.register_uri(httpretty.GET,
                               uri="https://reqres.in/api/users/2/",
                               body=json.dumps(read_body['data']))
        response = requests.get("https://reqres.in/api/users/2/")
        data = json.loads(response.text)
        assert data == read_body['data']

        httpretty.disable()
        httpretty.reset()

    @httpretty.activate(allow_net_connect=False)
    def test_new(self):
        read_body = Util.read_json_from_file('data.json')

        response = CustomRequests.get("https://reqres.in/api/users/2/", json.dumps(read_body['data']))
        data = json.loads(response.text)
        assert data == read_body['data']

        httpretty.disable()
        httpretty.reset()

    @allure.description("Positive auth user")
    def test_auth_user(self):
        httpretty.enable(verbose=True, allow_net_connect=False)

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

        # def setup(self):
        #     data = {"name": "morpheus",
        #             "job": "leader"
        #             }
        #     response = CustomRequests.get("/user/login", data=data)
        #     self.auth_sid = self.get_cookie(response, "auth_sid")
        #     self.token = self.get_header(response, "x-csrf-token")
        #     self.user_id_from_auth_method = self.get_json_value(response, "user_id")
        #     mock service with expected body response
