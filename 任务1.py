
list=[]
a = 0
for i in range(10):
    num = int(input("请输入数字"))
    list.append(num)
    print("第",i+1,"个数字是",num)
    a = list[i] + a
    if i == 9:
        print("列表中十个数字的和是：",a)


