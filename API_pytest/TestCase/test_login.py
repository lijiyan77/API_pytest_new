# -*- coding: UTF-8 -*-
# @File  : test_login.py
# author by : Li Jiyan
# date : 2020/4/9
import pytest
import allure
import json
from Conf.Config import Config
from Params.params import Login
from Common import Request, Assert


class TestLogin:
    @pytest.allure.feature('Home')
    @allure.severity('blocker')  # 按严重性级别来标记case
    @allure.story('Login')
    def test_login_01(self, action):
        """
        正常登录
        """
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        api_url = req_url + urls[0]

        params = data.data
        # print(params[0][0])

        response = request.post_request(api_url, params[0][0])
        re=json.loads(response)
        assert test.assert_text(re['data']['userName'], 'ouyangnana')

    def test_login_02(self, action):
        """
        密码错误
        """
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        api_url = req_url + urls[0]

        params = data.data
        # print(params[0][1])

        response = request.post_request(api_url, params[0][1])
        # print(response)
        re=json.loads(response)
        # print(re['data']['userName'])
        assert test.assert_text(re['message'], '登录账号或密码不正确')

    def test_login_03(self, action):
        """
        account错误
        """
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        api_url = req_url + urls[0]

        params = data.data
        # print(params[0][2])

        response = request.post_request(api_url, params[0][2])
        # print(response)
        re=json.loads(response)
        # print(re['data']['userName'])
        assert test.assert_text(re['message'], '登录账号或密码不正确')

    def test_login_04(self, action):
        """
        customerNo错误
        """
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        api_url = req_url + urls[0]

        params = data.data
        # print(params[0][2])

        response = request.post_request(api_url, params[0][3])
        # print(response)
        re=json.loads(response)
        # print(re['data']['userName'])
        assert test.assert_text(re['message'], '登录账号或密码不正确')



if __name__ == '__main__':
    pytest.main('-q test_login.py -p no:warnings' )
