a=[5,2,4,7,9,1,3,5,4,0,6,1,3]

for i in range(1, len(a)):
    for j in range(0, len(a)-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)