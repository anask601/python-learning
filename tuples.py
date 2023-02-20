# https://replit.com/@codewithharry/24-Day24-Introduction-to-Tuples#.tutorial/01-python_tuples.md
# https://replit.com/@codewithharry/24-Day24-Introduction-to-Tuples#.tutorial/02-tuple_indexes.md
tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

# create a tuple with a single element by including a trailing comma:
my_tuple = (1,)
print(my_tuple) # Output: (1,)

# create a tuple without using parentheses, by separating the elements with commas:
my_tuple = 1, 2, 3
print(my_tuple) # Output: (1, 2, 3)

# unpack a tuple into multiple variables:
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a) # Output: 1
print(b) # Output: 2
print(c) # Output: 3

# use tuples to return multiple values from a function:
def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age

result = get_name_and_age()
print(result) # Output: ("Alice", 30)
name, age = get_name_and_age()
print(name) # Output: "Alice"
print(age) # Output: 30


if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)
