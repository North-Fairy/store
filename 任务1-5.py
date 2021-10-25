import time

user = "root"
password = "admin"

for i in range(3):
    name = input("用户名：")
    pw = input("密码：")
    if name == "":
        print("请输入用户名")
    else:
        if user == name:
            if pw == password:
                print("登录成功")
                break
            else:
                print("密码错误")
        else:
            print("用户名错误")
    if  i == 2:
        print("您的账户被冻结五分钟，请稍后再试")
        time.sleep(300)