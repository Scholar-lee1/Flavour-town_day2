# Step 1: Crate an empty list
grocery_list  = []

# Step 2: Collect 5 items
print("Enter 5 grocery items")
for i in range(5):
    item = input(f"Item {i + 1}: ")
    grocery_list.append(item)

# Step 3: Display full list and length 
print("\nYour Grocery List")
print(grocery_list)
print(f"Total items: {len(grocery_list)}")

# Step 4: Remove an item
remove_item = input("Enter an item to remove from the list: ")
if remove_item in grocery_list:
    grocery_list.remove(remove_item)
    print(f"{remove_item} removed")
else:
    print(f"{remove_item} not found in the list")

# Step 5: Show first 3 item using slicing
print("\nFirst 3 items on your list:")
print(grocery_list[:3])

# Step 6: Display sorted list
print("\nSorted Grocery list")
print(sorted(grocery_list))