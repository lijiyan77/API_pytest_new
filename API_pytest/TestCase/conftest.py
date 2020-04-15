# -*- coding: UTF-8 -*-
# @File  : conftest.py
# author by : Li Jiyan
# date : 2020/4/9
"""

# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# @allure.severity #用于定义用例优先级
# @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址

# @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
# allure.environment(environment=env) #用于定义environment

"""

import allure
import pytest
import json

from Conf.Config import Config
from Common import Consts, Request
from Params.params import Login


@pytest.fixture()
def action():
    env = Consts.API_ENVIRONMENT_DEBUG

    conf = Config()
    host = conf.host_debug
    tester = conf.tester_debug
    allure.environment(environment=env)
    allure.environment(hostname=host)
    allure.environment(tester=tester)
    # print(env)
    return env


@pytest.fixture()
def login(action):
    conf = Config()
    data = Login()
    request = Request.Request(action)

    host = conf.host_debug
    req_url = 'http://' + host
    urls = data.url
    api_url = req_url + urls[0]

    params = data.data
    # print(params[0][0])

    response = request.post_request(api_url, params[0][0])
    re = json.loads(response)
    token = re['data']['token']
    pid=re['data']['id']
    # print(pid)
    return token,pid


if __name__ == '__main__':
    login(action)