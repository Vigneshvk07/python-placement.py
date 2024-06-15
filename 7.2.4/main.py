strA = input("Enter the first string: ")
strB = input("Enter the second string: ")

for char in strB:
    if char not in strA:
        print(char)
        break
