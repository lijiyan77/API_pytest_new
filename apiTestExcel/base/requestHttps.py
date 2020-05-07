# -*- coding: UTF-8 -*-
# @File  : requestHttps.py
# author by : Li Jiyan
# date : 2020/4/2

import requests
import json

'''封装post/get'''


class RunMain:
    def send_get(self, url, data):
        result = requests.get(url=url, params=data).json()
        res = json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
        return res

    def send_post(self, url, data):
        result = requests.post(url=url, data=json.dumps(data)).json()
        res = json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
        return res

    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'POST':
            result = self.send_post(url, data)
        elif method == 'GET':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result


if __name__ == '__main__':
    url = 'http://114.116.163.85:9997/api/hoolink-rpc/web/login'
    data = {
        "account": "ljy",
        "customerNo": "huling",
        "password": "2acb4dfb3e84c2c871260c51fe1101f8"
    }
    test = RunMain()
    print(test.run_main('POST', url, data))
