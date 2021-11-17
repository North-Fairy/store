r = open(file="baidu_x_system.log",mode="r+",encoding="utf-8")

data = r.readlines()
print(data)

one = 0
two = 0
three = 0
five = 0


for i in data:
    if "10.155.24.132" in i:
        one +=1
    elif "16.155.34.132" in i:
        two += 1
    elif "56.78.35.131" in i:
        three += 1
    elif "46.76.185.36" in i:
        five +=1
print(one,two,three,five)













