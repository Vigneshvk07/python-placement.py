def remove_repeated_chars(input_str):
    seen = set()
    result = ''
    
    for char in input_str:
        if char not in seen:
            result += char
            seen.add(char)
    
    return result

input_str = input("Enter a string: ")
result_str = remove_repeated_chars(input_str)

print("String after removing repeated characters:", result_str)
