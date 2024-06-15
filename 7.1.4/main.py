def string_length(input_str):
    return len(input_str)

def string_copy(input_str):
    return input_str

def string_concatenate(str1, str2):
    return str1 + str2

def string_to_uppercase(input_str):
    return input_str.upper()

def compare_strings(str1, str2):
    if str1 < str2:
        return "First string is alphabetically before second string."
    elif str1 > str2:
        return "First string is alphabetically after second string."
    else:
        return "Both strings are equal alphabetically."

# Main program
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print("Length of first string:", string_length(str1))
print("Length of second string:", string_length(str2))
print("Copy of first string:", string_copy(str1))
print("Concatenation of both strings:", string_concatenate(str1, str2))
print("Uppercase of first string:", string_to_uppercase(str1))
print(compare_strings(str1, str2))
