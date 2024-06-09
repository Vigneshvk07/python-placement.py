n = int(input("Enter array size: "))
if n <= 0:
    print("Invalid input")
else:
    print(f"Enter {n} array elements:")
    arr = list(map(int, input().split()))
    
    seen = set()
    repeated = None
    
    for num in arr:
        if num in seen:
            repeated = num
            break
        seen.add(num)
    
    if repeated is not None:
        print(f"The repetitive element: {repeated}")
    else:
        print("Array elements are not repeated")
