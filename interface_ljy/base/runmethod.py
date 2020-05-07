# -*- coding: UTF-8 -*-
# @File  : runmethod.py
# author by : Li Jiyan
# date : 2020/4/1

'''封装post/get'''

import requests
import json


class RunMain:
    def send_get(self, url, data):
        res = requests.get(url=url, params=data).json()
        # return res
        return json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False)

    def send_post(self, url, data):
        res = requests.post(url=url, data=json.dumps(data)).json()
        # return res
        return json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False)

    def run_main(self, url, method, data=None):
        if method == 'POST':
            res = self.send_post(url, data)
        else:
            res = self.send_get(url, data)
        return res