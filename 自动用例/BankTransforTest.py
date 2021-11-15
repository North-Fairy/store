from xlutils import copy
from 工商银行完整版 import bank_transformMoney
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

dae = readdata(3)

@ddt
class TestSave(TestCase):


    @data(*dae)
    @unpack
    def testsavemoney(self,a,b,c,d,e,i):

        result = bank_transformMoney(a,b,c,d)

        if result == e:
            table.get_sheet(3).write(i,5,"OK")
            table.save('bank.xls')
        else:
            table.get_sheet(3).write(i,5,"FAlse")
            table.save('bank.xls')

        self.assertEqual(result,    e)