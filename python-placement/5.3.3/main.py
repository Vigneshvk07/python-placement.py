n = int(input("Enter array size: "))
if n <= 0:
    print("Invalid array size")
else:
    print(f"Enter {n} sorted array elements:")
    arr = list(map(int, input().split()))
    
    last_duplicate_index = -1
    last_duplicate_item = None
    
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            last_duplicate_index = i
            last_duplicate_item = arr[i]
    
    if last_duplicate_index != -1:
        print(f"Last index: {last_duplicate_index}")
        print(f"Last duplicate item : {last_duplicate_item}")
    else:
        print("No duplicate found")
