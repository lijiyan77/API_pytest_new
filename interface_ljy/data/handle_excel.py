# -*- coding: UTF-8 -*-
# @File  : handle_excel.py
# author by : Li Jiyan
# date : 2020/4/1
'''封装Excel的读写'''


import xlrd
from xlutils.copy import copy


class HandleExcel:
    """封装操作Excel的方法"""

    def __init__(self, file='D:/hunter_/interfaceTest/hunter_interface/case/demo2.xlsx', sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()
        # 为了创建一个实例时就获得Excel的sheet对象，可以在构造器中调用get_data()
        # 因为类在实例化时就会自动调用构造器，这样创建一个实例时就会自动获得sheet对象了

    # 获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取Excel数据行数
    def get_rows(self):
        rows = self.data.nrows

        return rows

    # 获取某个单元格写入数据
    def get_value(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # 向某个单元格写入数据
    def write_value(self, row, col, value):
        data = xlrd.open_workbook(self.file)  # 打开文件
        data_copy = copy(data)  # 复制源文件
        sheet = data_copy.get_sheet(0)  # 取得复制文件的sheet对象
        sheet.write(row, col, value)  # 在某一单元格写入value
        data_copy.save(self.file)  # 保存文件


def get_caseNmber():
    caseNmber = 0
    return caseNmber


def get_caseType():
    caseType = 1
    return caseType


def get_caseName():
    caseName = 2
    return caseName


def get_priority():
    priority = 3
    return priority

def get_url():
    url = 4
    return url

def get_mothod():
    mothod = 5
    return mothod

def get_header():
    header = 6
    return header

def get_purpose():
    purpose = 7
    return purpose

def get_params():
    params = 8
    return params

def get_expectvalue():
    expectvalue = 9
    return expectvalue

def get_actualvalue():
    actualvalue = 10
    return actualvalue

def get_resultvalue():
    resultvalue = 11
    return resultvalue