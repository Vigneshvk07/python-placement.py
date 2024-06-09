n = int(input("Enter how many values you want to read: "))
array = []

for i in range(n):
    value = int(input(f"Enter the value of a[{i}] : "))
    array.append(value)

for i in range(n):
    for j in range(i + 1, n):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print("Array sorted in ascending order =", ' '.join(map(str, array)))
