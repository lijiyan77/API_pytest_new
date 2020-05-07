# -*- coding: UTF-8 -*-
# @File  : Session.py
# author by : Li Jiyan
# date : 2020/4/9
from Conf import Config
from Common import Log
import requests

class Session:
    def __init__(self):
        self.config=Config.Config()
        self.log = Log.MyLog()

    def get_session(self,env):
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/75.0.3770.100 Safari/537.36",
            "Content-Type": "application/json"
        }

        if env=='debug':
            login_url = 'https://' + self.config.host_debug+self.config.loginHost_debug
            # print(login_url)
            parm = self.config.loginInfo_debug

            session_debug = requests.session()
            response = session_debug.post(login_url, parm, headers=headers)
            # print(response.cookies)
            self.log.debug('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()

        else:
            print("get cookies error")
            self.log.error('get cookies error, please checkout!!!')


if __name__ == '__main__':
    ss = Session()
    ss.get_session('debug')