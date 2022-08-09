import allure
import httpretty
import requests

from lib.logger import Logger


class CustomRequests:

    # python -m pytest --alluredir=test_results/ tests/test_user_auth.py
    # allure serve test_results

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request to URL: {url}"):
            return CustomRequests._send(url, data, headers, cookies, 'GET')

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):

        with allure.step(f"POST request to URL: {url}"):
            return CustomRequests._send(url, data, headers, cookies, 'POST')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request to PUT: {url}"):
            return CustomRequests._send(url, data, headers, cookies, 'PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request to DELETE: {url}"):
            return CustomRequests._send(url, data, headers, cookies, 'DELETE')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):

        base_url = "https://reqres.in/"
        url = f"https://reqres.in/{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)

        if method == 'GET':
            httpretty.register_uri(httpretty.GET, uri=base_url, body=data)
            response = requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            httpretty.register_uri(httpretty.POST, uri=base_url, body=data)
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == 'PUT':
            httpretty.register_uri(httpretty.PUT, uri=base_url, body=data)
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            httpretty.register_uri(httpretty.DELETE, uri=base_url, body=data)
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return response
