def is_multiple_of_3(binary_str):
    decimal = int(binary_str, 2)
    return decimal % 3 == 0

binary_str = input("Enter binary characters: ")

if is_multiple_of_3(binary_str):
    print("Yes")
else:
    print("No")
