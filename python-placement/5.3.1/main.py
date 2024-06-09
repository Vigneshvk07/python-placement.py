import math

n = int(input("Enter array size: "))
if n <= 0:
    print("Invalid input")
else:
    print(f"Enter {n} array elements:")
    arr = list(map(int, input().split()))
    
    largest_non_square = -1
    
    for num in arr:
        if math.isqrt(num) ** 2 != num and num > largest_non_square:
            largest_non_square = num
    
    if largest_non_square != -1:
        print(largest_non_square)
    else:
        print("No number is not a perfect square")
