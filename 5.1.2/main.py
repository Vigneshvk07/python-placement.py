a=int(input())
b=[None]*a
for i in range(0,a):
    print("value{}=".format(i+1),end="")
    b[i]=int(input())
print("value you want to check=",end="")
c=int(input())
yes=0
for i in range(0,a):
    if(b[i]==c):
        yes=yes+1
if(yes==1):
    print("yes")
else:
    print("no")
    
