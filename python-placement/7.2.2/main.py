def compress_string(input_str):
    n = len(input_str)
    if n <= 1:
        return input_str
    
    compressed = ''
    count = 1

    for i in range(1, n):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed += input_str[i - 1] + str(count)
            count = 1
    
    compressed += input_str[n - 1] + str(count)

    if len(compressed) < n:
        return compressed
    else:
        return input_str


input_str = input("Enter a string: ")
compressed_str = compress_string(input_str)
print("Compressed string:", compressed_str)
