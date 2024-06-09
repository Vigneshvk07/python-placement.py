n = int(input("Enter the array size: "))
print(f"Input {n} elements in an array:")
array = []

for _ in range(n):
    element = int(input())
    array.append(element)

unique_elements = []
seen_elements = set()

for element in array:
    if element not in seen_elements:
        unique_elements.append(element)
        seen_elements.add(element)

print("The unique elements found in the array are:")
for element in unique_elements:
    print(element, end=' ')
