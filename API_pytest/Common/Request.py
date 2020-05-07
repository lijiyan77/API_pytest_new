# -*- coding: UTF-8 -*-
# @File  : Request.py
# author by : Li Jiyan
# date : 2020/4/9
import requests
import json

import Common
from Common import Session
from Common import Consts


class Request:
    def __init__(self,env):
        self.session=Session.Session()
        self.get_session=self.session.get_session(env)

    def post_request(self, url, data=None,header=None):
        result = requests.post(url=url, data=json.dumps(data),headers=header).json()
        res = json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
        return res

        # time_consuming为响应时间，单位为毫秒
        time_consuming = res.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = res.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = res.status_code
        try:
            response_dicts['body'] = res.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = res.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

if __name__ == '__main__':
    url = 'https://api.test.hoolink.com/api/hoolink-rpc/web/login'
    data = {
        "account": "ljy",
        "customerNo": "huling",
        "password": "2acb4dfb3e84c2c871260c51fe1101f8"
    }
    header={'Content-Type': 'application/json'}

    test = Request(Consts.API_ENVIRONMENT_DEBUG)
    print(test.post_request(url,data,header))