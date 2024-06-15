def display_array(arr):
    print("Array elements:", ' '.join(map(str, arr)))

def insert_number(arr, num, loc):
    if loc < 1 or loc > len(arr) + 1:
        print("Invalid location")
    else:
        arr.insert(loc - 1, num)
        print(f"{num} inserted at location {loc}")

def delete_number(arr, loc):
    if loc < 1 or loc > len(arr):
        print("Invalid location")
    else:
        removed = arr.pop(loc - 1)
        print(f"{removed} deleted from location {loc}")


size = int(input("Enter size: "))
print(f"Enter {size} elements:")
arr = list(map(int, input().split()))
    
display_array(arr)
    
while True:
    print("\n1. Insert a number")
    print("2. Delete a number")
    print("3. Exit")
        
    choice = int(input("Enter your choice: "))
        
    if choice == 1:
        loc = int(input("Location: "))
        num = int(input("Number: "))
        insert_number(arr, num, loc)
    elif choice == 2:
        loc = int(input("Location: "))
        delete_number(arr, loc)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
        
    display_array(arr)


