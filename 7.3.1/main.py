def largest_subsequence(s, k):
    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1
    
    t = ''
    for char in s:
        if freq_map[char] >= k and char not in t:
            t += char
    
    return t

input_str = input("Enter the any string: ")
k = int(input("Enter any number: "))

result_str = largest_subsequence(input_str, k)
print(result_str)
