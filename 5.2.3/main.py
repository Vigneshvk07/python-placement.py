n = int(input("Enter how many values you want to read: "))
array = []
sum=0
for i in range(n):
    value = int(input(f"Enter the value of a[{i}] : "))
    array.append(value)
    sum+=value


print("The sum of array elements =", sum)
