from 工商银行完整版 import bank_addUser
from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import  unpack
import xlrd
from xlutils import copy
from READ import readdata

wd = xlrd.open_workbook(r'HKR.xlsx',encoding_override=True)

table = copy.copy(wd)
# print(file)

dae = readdata(0)

@ddt
class TestSave(TestCase):


    @data(*dae)
    @unpack
    def testsavemoney(self,a,b,c,d,e,f,g,ex,i):

        result = bank_addUser(a,b,c,d,e,f,g)

        if result == ex:
            table.get_sheet(0).write(i,8,"OK")
            table.save('bank.xls')
        else:
            table.get_sheet(0).write(i,8,"FAlse")
            table.save('bank.xls')

        self.assertEqual(result,    ex)




















