a=int(input())
b=[None]*a
for i in range(0,a):
    print("value{}=".format(i+1),end="")
    b[i]=int(input())
for i in range(0,a):
    for j in range(i+1,a):
        if(b[i]>b[j]):
            b[i],b[j]=b[j],b[i]
print("largest number={}".format(b[a-1]))
print("smallest number={}".format(b[0]))