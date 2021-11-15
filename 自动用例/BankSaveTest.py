from xlutils import copy
from 工商银行完整版 import bank_saveMoney
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from READ import readdata
# import xlwt
import xlrd

wd = xlrd.open_workbook(r'HKR.xlsx',encoding_override=True)

table = copy.copy(wd)
# print(file)

dae = readdata(1)

@ddt
class TestSave(TestCase):


    @data(*dae)
    @unpack
    def testsavemoney(self,a,s,e,i):

        result = bank_saveMoney(a,s)

        if result == e:
            table.get_sheet(1).write(i,3,"OK")
            table.save('bank.xls')
        else:
            table.get_sheet(1).write(i,3,"FAlse")
            table.save('bank.xls')

        self.assertEqual(result,    e)

        # try:
        #     fh = open("test.text","w",encoding="utf-8")
        #
        #     fh.write("测试文件,检测异常")
        # except IOError:
        #     print("ERRP:没有文件或读取失败")
        # else:
        #     print("内容写入成功")
        #     fh.close()



















