# -*- coding: UTF-8 -*-
# @File  : RunTestCase.py
# author by : Li Jiyan
# date : 2020/4/3
from base.requestHttps import RunMain
from data.HandleExcel import *
from data.logger import Logger
import json


class RunTestCase:
    def __init__(self):
        self.Runmain = RunMain()  # 实例化调用get/post请求基类
        self.data = HandleExcel()
        self.logger = Logger(__name__)

    def go_run(self):
        rows_count = self.data.get_rows()
        for i in range(1, rows_count):
            url = self.data.get_value(i, HandleExcel.get_url())
            method = self.data.get_value(i, HandleExcel.get_mothod())
            """python从excel中解析出来的数据类型不是字典，是字符串，所以无法传递给requests当做请求参数
                需用用json.loads()转成字典格式，然后进行传参"""
            data = json.loads(self.data.get_value(i, HandleExcel.get_params()))
            # data1 = self.data.get_value(i, HandleExcel.get_params())
            # data=json.loads(data1)
            expect=self.data.get_value(i,HandleExcel.get_expectvalue())

            is_run=self.data.get_value(i,HandleExcel.get_priority())
            if is_run =='high':
                res = self.Runmain.run_main(url, method, data)
                self.logger.get_log().debug('第' + str(i) + '个接口的返回结果为：%s', res)
                self.data.write_value(i, HandleExcel.get_actualvalue(), res)

                if expect in res:
                    # print('测试通过')
                    self.logger.get_log().error('第' + str(i) + '接口测试通过')
                    self.data.write_value(i, HandleExcel.get_resultvalue(), 'pass')
                else:
                    # print('测试失败')
                    self.logger.get_log().info('第' + str(i) + '接口测试失败')
                    self.data.write_value(i, HandleExcel.get_resultvalue(), 'fail')
                # print('=====')


if __name__ == '__main__':
    run = RunTestCase()
    run.go_run()
