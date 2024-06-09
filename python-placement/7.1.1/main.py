def count_char_frequency(input_str):
    frequency = {}
    
    for char in input_str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency

input_str = input("Enter a string: ")
frequency = count_char_frequency(input_str)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
