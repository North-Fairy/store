N = int(input("请输入数字："))
i=0
while i<N:
    j=1
    while j<=i+1:
        print("%d*%d=%d"%(j,i+1,j*(i+1)),end="   ")
        j+=1
    print()
    i+=1