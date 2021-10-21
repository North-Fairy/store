"""
随机点名然后处罚遍数
#优化代码：只有一个input 进行判断 1or2 生成人名or几遍    q or Q退出  输入其他的直接锁死time.sleep(10)睡10秒
"""
import random
import time

list=["法外狂徒","小李子","汤老师","郭达","强森","抖森","小罗伯特","汉弗莱","兰尼斯特","千纸鹤"]
print("输入1：随机人名，输入2：随机处罚的遍数，输入q或者Q：退出，输入其他的锁死十秒")

while True:
    index = input("请输入您需要进行的操作：")

    if index == "1":
        dint = random.randint(0,len(list)-1)
        print(list[dint])

    elif index == "2":
        num = random.randint(0,10)
        print(list[dint],"被处罚了",num,"遍")

    elif index == "q" or "Q":
        break

    else:
        time.sleep(10)
