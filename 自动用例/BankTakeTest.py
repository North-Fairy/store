from xlutils import copy
from 工商银行完整版 import bank_takeMoney
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

dae = readdata(2)

@ddt
class TestSave(TestCase):


    @data(*dae)
    @unpack
    def testsavemoney(self,a,b,c,d,i):

        result = bank_takeMoney(a,b,c)

        if result == d:
            table.get_sheet(2).write(i,4,"OK")
            table.save('bank.xls')
        else:
            table.get_sheet(2).write(i,4,"FAlse")
            table.save('bank.xls')

        self.assertEqual(result, d)