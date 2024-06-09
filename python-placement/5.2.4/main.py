n = int(input("Enter how many values you want to read: "))

a = []
b = []

for i in range(n):
    value_a = int(input(f"Enter the value of a[{i}] : "))
    a.append(value_a)

for i in range(n):
    value_b = int(input(f"Enter the value of b[{i}] : "))
    b.append(value_b)

if a == b:
    print("Both arrays are equal")
else:
    print("Both arrays are not equal")
