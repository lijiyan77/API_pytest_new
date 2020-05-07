# -*- coding: UTF-8 -*-
# @File  : HandleExcel.py
# author by : Li Jiyan
# date : 2020/4/3

import xlrd
from xlutils.copy import copy

class HandleExcel:
    '''封装操作Excel的方法'''

    def __init__(self,file='C:/Users/Administrator/PycharmProjects/apiTestExcel/case/demo2.xls',sheet_id=0):
        self.file = file
        self.sheet_id=sheet_id
        self.data=self.get_data()
        # 为了创建一个实例时就获得Excel的sheet对象，可以在构造器中调用get_data()
        # 因为类在实例化时就会自动调用构造器，这样创建一个实例时就会自动获得sheet对象了

    # 获取某一页sheet对象
    def get_data(self):
        data=xlrd.open_workbook(self.file)
        sheet=data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取Excel数据行数
    def get_rows(self):
        rows=self.data.nrows

        return rows

    # 获取Excel数据列数
    def get_cols(self):
        cols=self.data.ncols

        return cols

    # 获取某个单元格写入数据
    def get_value(self,row,col):
        value=self.data.cell_value(row,col)
        return value

    # 向某个单元格写入数据
    def write_value(self,row,col,value):
        data=xlrd.open_workbook(self.file)
        data_copy=copy(data)    # copy的参数，是对应的workbook，而不是file
        sheet=data_copy.get_sheet(0)
        sheet.write(row, col, value)
        data_copy.save(self.file)

    # 封装Excel的列名常量
    def get_caseseq():
        caseSeq=0
        return caseSeq

    def get_apiType():
        apiType=1
        return apiType

    def get_apiseq():
        apiSeq=2
        return apiSeq

    def get_apiname():
        apiName=3
        return apiName

    def get_priority():
        priority = 4
        return priority

    def get_url():
        url = 5
        return url

    def get_mothod():
        mothod = 6
        return mothod

    def get_header():
        header = 7
        return header

    def get_purpose():
        purpose = 8
        return purpose

    def get_params():
        params = 9
        return params

    def get_expectvalue():
        expectValue = 10
        return expectValue

    def get_actualvalue():
        actualValue = 11
        return actualValue

    def get_resultvalue():
        resultValue = 12
        return resultValue


if __name__ == '__main__':
    test=HandleExcel()
    print(test.get_data())
    print(test.get_rows())
    print(test.get_value(1,1))