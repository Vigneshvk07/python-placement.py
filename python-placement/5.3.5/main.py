n = int(input("Enter array size: "))
if n <= 0:
    print("Invalid input")
else:
    print(f"Enter {n} array elements:")
    arr = list(map(int, input().split()))
    
    count_zeros = 0
    
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[count_zeros] = arr[count_zeros], arr[i]
            count_zeros += 1
    
    print(' '.join(map(str, arr)))
