# -*- coding: UTF-8 -*-
# @File  : run_test.py
# author by : Li Jiyan
# date : 2020/4/1


# from conn.run_demo import RunMain
from data.handle_excel import *
from data.logger import Logger
import json
from base.runmethod import RunMain


class RunTestCase:
    def __init__(self):

        self.Runmain = RunMain()
        self.data = HandleExcel()
        self.logger = Logger(__name__)

    def go_run(self):
        rows_count = self.data.get_rows()  # 获取Excel行数
        for i in range(1, rows_count):
            url = self.data.get_value(i, get_url())  # 循环获取URL的值
            method = self.data.get_value(i, get_mothod())  # 循环获取method的值
            print(self.data.get_value(i, get_params()))
            data = json.loads(self.data.get_value(i, get_params()))
            expect = self.data.get_value(i, get_expectvalue())
            is_run = self.data.get_value(i, get_priority())
            if is_run == 'high':
                res = self.Runmain.run_main(url, method, data)
                self.logger.get_log().debug('第' + str(i) + '个接口的返回结果为：%s', res)  # 日志：输出接口响应内容
                self.data.write_value(i, get_actualvalue(), res)  # 将实际结果写入Excel中
                if expect in res:  # res返回的内容是否包含expect，是否与期望一致
                    print((expect))
                    print(type(expect))
                    print((res))
                    print(type(res))
                    print('测试通过')
                    self.logger.get_log().error('第' + str(i) + '接口测试通过')
                    self.data.write_value(i, get_resultvalue(), 'pass')  # 调用写入数据方法，将结果写进Excel
                else:
                    # print("测试失败")
                    self.logger.get_log().info('第' + str(i) + '接口测试失败')
                    self.data.write_value(i, get_resultvalue(), 'fail')


if __name__ == '__main__':
    run = RunTestCase()
    run.go_run()