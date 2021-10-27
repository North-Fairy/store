import random

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank_name="迪迦银行"#全局变量
bank={'Frank': {'password': '123456', 'country': '中国', 'province': '沙河', 'street': '老牛湾', 'door': '0001', 'account': 60547549, 'bank_name': '迪迦银行', 'money': 100}}
#{'Frank': {'password': '123456', 'country': '中国', 'province': '沙河', 'street': '老牛湾', 'door': '0001', 'account': 60547549, 'bank_name': '汉科软地球中国区老牛湾分行', 'money': 0}}
#                 元素1   ，元素 2 ，元素3
def bank_useradd(username,password,country,province,street,door,account):
    bank[username]={
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "account":account,
        "bank_name":bank_name,
        "money":0
    }
    return 1

def useradd():
    while True:
        username = input("请输入您的用户名")
        password = input("请输入您的六位密码")  # print(bank[username]["password"])
        if len(password) == 6:
            print("下面请您输入你的地址")
            country = input("\t\t请输入你所在的国家")
            province = input("\t\t请输入您的省份")
            street = input("\t\t请输入你的街道")
            door = input("\t\t请输入您的门牌号")
            account = random.randint(10000000, 99999999)

            #             元素1    元素2    元素3
            status = bank_useradd(username, password, country, province, street, door, account)
            if status == 1:
                print("恭喜你成功开户，以下是您的信息")
                info = '''
                            ------------个人信息------------
                            用户名:%s
                            账号：%s
                            密码：*****
                            国籍：%s
                            省份：%s
                            街道：%s
                            门牌号：%s
                            余额：%s
                            开户行名称：%s
                        '''
                # 每个元素都可传入%
                print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
                break
        else:
            print("请输入六位密码")
#存钱
def save():
    name= input("请输入您的名称：")
    for i in bank:
        if name == i:
            pw = input("请输入您的六位密码")
            if pw == bank[i]["password"]:
                print("登录成功")
                money1 =int(input("请输入您要存入的金额："))
                bank[i]["money"]+= money1
                print("您当前余额为：",bank[i]["money"])
            else:
                print("密码输入错误，请重试")
        else:
            continue

# #取钱
def withdraw():
    name= input("请输入您的名称：")
    for i in bank:
        if name == i:
            pw = input("请输入您的六位密码")
            if pw == bank[i]["password"]:
                print("登录成功")
                money1 =int(input("请输入您要取出的金额："))
                if money1<=bank[i]["money"]:
                    bank[i]["money"]-= money1
                    print("您当前余额为：",bank[i]["money"])
                else:
                    print("您当前余额不足")
            else:
                print("密码输入错误，请重试")
        else:
            continue



# #转账
def transfer():
    name = input("请输入您的名称：")
    for i in bank:
        if name == i:
            pw = input("请输入您的六位密码：")
            if pw == bank[i]["password"]:
                print("登录成功")
                money1 = int(input("请输入您要转账的金额："))
                name1 = input("请输入您要转账的对象：")
                id = int(input("请输入您要转账用户的账号："))
                for j in bank:
                    if j == name1:
                        if bank[j]["account"] == id:
                            bank[i]["money"] -= money1
                            bank[j]["money"] += money1
                            print("转账成功，您当前余额为：", bank[i]["money"])
                        else:
                            print("请检查您需要转账的账号是否正确")
            else:
                print("密码输入错误，请重试")
        else:
            continue
#查询
def query():
    name = input("请输入您的名称：")
    for i in bank:
        if i == name :
            info = '''
                                ------------个人信息------------
                                用户名:%s
                                账号：%s
                                密码：*****
                                国籍：%s
                                省份：%s
                                街道：%s
                                门牌号：%s
                                余额：%s
                                开户行名称：%s
                            '''
            # 每个元素都可传入%
            print(info % (name, bank[i]["account"], bank[i]["country"], bank[i]["province"],  bank[i]["street"], bank[i]["door"], bank[i]["money"], bank_name))



while True:
    begin = input("请选择业务：")
    if begin == "1":
        useradd()
    elif begin == "2":
        withdraw()
    elif begin == "3":
        save()
    elif begin == "4":
        transfer()
    elif begin == "5":
        query()
    elif begin == "6":
        print("退出系统")
        break
