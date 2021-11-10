import time
from threading import Thread

#篮子
num = 0
#收银员
money = 0

#厨师
class cook(Thread):
    name = ""
    user1 = 0

    time1 = 0
    def run(self) -> None:
        while True:
            global num
            if num <= 500:
                self.user1 += 1
                num += 1
            else:
                time.sleep(3)
                self.time1 += 3
                if self.time1 == 180:
                    print(self.name,"制作了",self.user1,"个蛋挞","赚了",self.user1*2.5,"元")
                    break
            print(num)
            print("厨师1制作了",self.user1,"个蛋挞")

#窗口
class user(Thread):
    name = ''
    money2 = 5000
    egg = 0
    count = 0

    def run(self) -> None:
        while time.perf_counter() <= 100:
            global num
            global money
            if self.money2 > 0:
                if num > 0:
                    self.money2 -= 3
                    self.egg += 1
                    num -= 1
                    money += 3
                    print(self.name, self.money2)
                elif num == 0:
                    print('没了')
                    time.sleep(4)
            else:
                print('没钱了')
                break
        print(self.name, '还剩', self.money2)


c1 = cook()
c3 = cook()
c2 = cook()
c1.name = "张三"
c2.name = "李四"
c3.name = "王五"


c1.start()
c2.start()
c3.start()


u1 = user()
u2 = user()
u3 = user()
u4 = user()
u5 = user()
u6 = user()

u1.name = "用户1"
u2.name = "用户2"
u3.name = "用户3"
u4.name = "用户4"
u5.name = "用户5"
u6.name = "用户6"

u1.run()
u2.run()
u3.run()
u4.run()
u5.run()
u6.run()