# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
# print(names[0][5])
num = 0
year = 0
for i in range(len(names)):
    num += names[i][5]
    year += int(names[i][1])
num= num/(i+1)
year = year/(i+1)
print("每个人平均工资是：",num)
print("每个人平均年龄是：",year)

names.append(["刘备","45","男","220","alibaba",500,"30"])
print(names)

man = 0
woman = 0
sum = 0
bu1=0
bu2=0
bu3=0
bu4=0
while True:
    if names[sum][6]=="50":
        bu1 += 1
    elif names[sum][6]=="60":
        bu2 += 1
    elif names[sum][6]=="10":
        bu3 += 1
    elif names[sum][6]=="30":
        bu4 += 1

    if names[sum][2] == "男":
        man += 1
        sum+=1
    elif names[sum][2] == "女":
        woman += 1
        sum+=1
    if sum == len(names):
        break


print("男宾",man,"位","女宾",woman,"位")
print("部门编号为50的人有：",bu1,"位")
print("部门编号为60的人有：",bu2,"位")
print("部门编号为10的人有：",bu3,"位")
print("部门编号为30的人有：",bu4,"位")
