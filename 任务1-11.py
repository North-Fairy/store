# num = int(input("请输入数字: "))
#
# fac = 1
# i = 1
#
# while i <= num:
#     fac = fac * i
#     i = i + 1
#
# print("数字 ", num, " 的阶乘是 ", fac)


num = int(input("请输入数字: "))

fac = 1

for i in range(1, num + 1):
    fac = fac * i

print("数字 ", num, " 的阶乘是 ", fac)