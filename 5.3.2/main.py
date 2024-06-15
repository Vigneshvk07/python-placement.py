def count_subsets(arr):
    n = len(arr)
    return 2 ** n

n = int(input("Enter array size: "))
if n <= 0:
    print("Invalid input")
else:
    print(f"Enter {n} elements:")
    arr = list(map(int, input().split()))
    subsets_count = count_subsets(arr)
    print(subsets_count)
