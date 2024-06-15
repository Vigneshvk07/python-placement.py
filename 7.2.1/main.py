def compare_strings(str1, str2):
    if str1 == str2:
        return f"{str1} is equal to {str2}"
    elif str1 > str2:
        return f"{str1} is greater than {str2}"
    else:
        return f"{str1} is less than {str2}"

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = compare_strings(str1, str2)
print(result)
