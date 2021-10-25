list=[]
a = 0
max=0
for i in range(10):
    num = int(input("请输入第{}个数字".format(i+1)))
    list.append(num)

    a = num + a

    if max < num:
        max=num

b=a/len(list)
print("列表中十个数字的和是：",a)
print("列表中十个数字的平均数是：",b)
print("列表中最大的数字是：",max)