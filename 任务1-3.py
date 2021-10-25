while True:
    a = int(input("输入第一条边"))
    b = int(input("输入第二条边"))
    c = int(input("输入第三条边"))
    if a+b>c and a+c>b and c+b>a and c-a<b and a-b<c and b-c<b:
         print("是三角形")
         if a == b == c:
             print("等边三角形")
         elif a == b:
             print("等腰三角形")
         elif a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b:
             print("直角三角形")
         else:
             print("普通三角形")
    else:
        print("输入的三条边不构成三角形")
        break
