# -*- coding: UTF-8 -*-
# @File  : test_login.py
# author by : Li Jiyan
# date : 2020/4/9


import pytest
import allure
import json
from Conf.Config import Config
from Params.params import Get
from Common import Request, Assert
from TestCase.conftest import login
from Common import Consts


class TestGet:
    @pytest.allure.feature('Home')
    @allure.severity('blocker')  # 按严重性级别来标记case
    @allure.story('Get')
    def test_get_01(self, action):
        """
        获取个人信息
        """
        conf = Config()
        data = Get()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        api_url = req_url + urls[0]
        params = data.data
        header = {'X-Token': login(action)[0]}

        response = request.post_request(api_url, params[0], header)
        print(response)
        re = json.loads(response)
        assert test.assert_text(re['data']['customerNo'], Consts.API_CUSTOMERNO)


if __name__ == '__main__':
    pytest.main('-q test_get.py -p no:warnings')
