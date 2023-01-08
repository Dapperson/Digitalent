# The inner life of lists
from re import L


list_1 = [1]
list_2 = list_1
list_1[0] = 2

print(list_1)


# Powerful slices

# Copying the entire list
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


# Slices - negative indices
'''
my_list = [start: end]
'''

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1: 1]
print(new_list)


# Slices: continued
'''
my_list = [:end]
my_list = [0:end]

my_list[start:]
my_list[start:len(my_list)]
'''

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)


# Lists - some simple programs
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i
        
print(largest)

###

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i
        
print(largest)

###

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

###

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")
    
###

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

###

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = [] # The helping list inside which we will add only unique numbers

for i in my_list:
    if i not in new_list: # The comparison part
        new_list.append(i) # Only ubique numbers will be added. Duplicates wont.
my_list = new_list # To update the original list. Or, you can print the new_list instead.

print("The list with unique elements only:")
print(my_list)


#Key takeaways

# 1. point to one and the same list in memory
vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']

# 2. slicing
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

# 3. negative indicies
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

# 4. optional
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

# 5. delete slices
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []

# 6. exist in a list or not
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False

