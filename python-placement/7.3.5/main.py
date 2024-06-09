def remove_consonants(input_str):
    vowels = "aeiou"
    result_str = ""
    
    for char in input_str:
        if char in vowels:
            result_str += char
    
    return result_str

input_str = input("Enter the input string: ")
output_str = remove_consonants(input_str)

print("The output string:", output_str)
