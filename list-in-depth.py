
# Slicing:
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4]) # Output: [2, 3, 4]
print(my_list[:3]) # Output: [1, 2, 3]
print(my_list[3:]) # Output: [4, 5]
# Length:
my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # Output: 5
# Membership:
my_list = ["apple", "banana", "cherry"]
if "apple" in my_list:
    print("Yes")
else:
    print("No")
# Output: "Yes"
# Removing elements:
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")
print(my_list) # Output: ["apple", "cherry"]

my_list = ["apple", "banana", "cherry"]
del my_list[0]
print(my_list) # Output: ["banana", "cherry"]
# Sorting:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort()
print(my_list) # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort(reverse=True)
print(my_list) # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]
# Copying:
my_list = ["apple", "banana", "cherry"]
new_list = my_list.copy()
print(new_list) # Output: ["apple", "banana", "cherry"]
# List comprehension:
my_list = [1, 2, 3, 4, 5]
new_list = [x**2 for x in my_list]
print(new_list) # Output: [1, 4, 9, 16, 25]