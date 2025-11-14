# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
my_list = [1, 2, 3, 4, 5] 
print(my_list) # 1, 2, 3, 4, 5.
print(type(my_list)) # <class 'list'>

# accessing elements
print(my_list[0])
print(my_list[1:4])
print(my_list[0:])

# modifying lists
# addding item to the end of the list
my_list.append(6)
print(my_list)
my_list.extend([10, 11, 12, 13, 14])
print(my_list)

# add 500 more numbers to the list
my_list.extend(list(range(15, 515)))
print(my_list)
my_list.extend(list(range(515, 1115)))
print(my_list)

# instead of creating separate variable we can put them in a list
# this makes hte job easier when we need to
# manage multiple variables
# performance task answer.

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.