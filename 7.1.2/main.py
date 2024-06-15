def replace_first_occurrence(input_str, char_to_replace, replacement_char):
    result = ''
    replaced = False
    
    for char in input_str:
        if char == char_to_replace and not replaced:
            result += replacement_char
            replaced = True
        else:
            result += char
    
    return result

input_str = input("Enter a string: ")
char_to_replace = input("Enter the character to replace: ")
replacement_char = input("Enter the replacement character: ")

result_str = replace_first_occurrence(input_str, char_to_replace, replacement_char)
print("Resultant string:", result_str)
