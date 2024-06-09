def max_min_product(arr1, arr2):
    max_first = max(arr1)
    min_second = min(arr2)
    product = max_first * min_second
    return max_first, min_second, product

size1, size2 = map(int, input("Enter size of first and second arrays: ").split())
if size1 <= 0 or size2 <= 0:
    print("Invalid array size")
else:
    print(f"Enter {size1} first array elements:")
    first_array = list(map(int, input().split()))
    print(f"Enter {size2} second array elements:")
    second_array = list(map(int, input().split()))
    
    max_elem, min_elem, result = max_min_product(first_array, second_array)
    
    print(f"Max element in first array is {max_elem} and min element in second array is {min_elem}")
    print(f"The product of these two is {result}")

