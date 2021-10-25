num = 20 #井的高度
num1 = 1 #天数
up=3 #上升的高度
down=2 #下降的高度
while True:
    if num1 * 3 - (num1-1) * 2 >= num:
        print("第%d天出来的"%num1)
        break
    elif num1 * 3 - num1 * 2 >= num:
        print("第%d天出来的"%num1)
        break
    else:
        num1+=1