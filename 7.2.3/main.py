def strcpy_recursive(dest, src, index=0):
    if index == len(src):
        return dest
    dest += src[index]
    return strcpy_recursive(dest, src, index + 1)

first_str = input("Enter first string: ")
second_str = input("Enter second string: ")

result_str = strcpy_recursive('', first_str)
print("After copy the First string:", result_str)
print("Second string:", result_str)
