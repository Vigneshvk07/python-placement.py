def longest_word_length(input_str):
    words = input_str.split()
    longest_word = max(words, key=len)
    return len(longest_word)

input_str = input("Enter a string: ")
result = longest_word_length(input_str)
print("Longest word's length =", result)


