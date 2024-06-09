a=int(input())
b=[None]*a
for i in range(0,a):
    print("number",i,"=",end="")
    b[i]=int(input())
print(b)