'''
猜字游戏：
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
#任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出
'''
import random
#              20，10
randint=random.randint(10, 20)#随机生成数字的范围：int   []
print(randint)
i=5
sum=0

while sum<3:
    if i<=0:
        break
    else:
        if sum == 2:
            print("这是您最后一次机会，这次答错了会直接扣除 3 枚金币")
            num = int(input("请输入您猜的数字"))
            if num == randint:
                print("恭喜你猜对了")
                print("恭喜你猜对了，你还有", i, "枚金币")
                break  # 退出
            else:
                i -= 3
                print("您还是没回答对，本次扣除一枚金币，你还有", i, "枚金币")
                break
        else:
            num = int(input("请输入您猜的数字"))
            if num == randint:
                print("恭喜你猜对了你还有", i, "枚金币")
                break  # 退出

            elif num > randint:
                i -= 1
                print("本次扣除一枚金币，你还有", i, "枚金币")
                print("猜的大了")

            elif num < randint:
                i -= 1
                print("本次扣除一枚金币，你还有", i, "枚金币")
                print("猜的小了")
    sum+=1


