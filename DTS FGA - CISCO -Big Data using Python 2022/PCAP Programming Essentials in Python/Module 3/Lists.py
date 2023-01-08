#collections of data
numbers = [10, 5, 7, 2, 1]

#collections of data | indexing
numbers = [10, 5, 7, 2, 1]
print("Original lists content: ", numbers) # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4] # Copying value of the fifth element to the second.
print("\nNew list content :", numbers) # Printing current list content.

#Accessing list content
print("\nList length numbers :", len(numbers)) # Printing the lists length

#collections data | operations on list
#Removing elements from a list
del numbers[1] # Removing the second elements from the list
print("\nNew list length: ", len(numbers))
print("\nNew list content: ", numbers)

#Negative indices are legal
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])


hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Input new number: "))

# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]

# Step 3: write a line of code that prints the length of the existing list
print(len(hat_list))

print(hat_list)


#collections of data | Functions and methods
'''
result = function(arg)
result = data.method(arg)
'''

#collections of data | list methods
#Adding elements to a list: append() and insert()
'''
list.append(value)
list.insert(location, value)
'''

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4)
print(len(numbers))
print(numbers)

numbers.inser(0, 222)
print(len(numbers))
print(numbers)


#Adding elements to a list: continued
my_list = [] # Creating an empty list

for i in range(5):
    my_list.append(i + 1)
print(my_list)


#collections of data | lists and loops
#Making use of lists
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]
print(total)


#Lists in action
variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2

###

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

###

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1


my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)


my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range (length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print(my_list)    


#step 1: create an empty list named beatles;
beatles = []
print("Step 1:", beatles)

#step 2: use the append() method to add the following members of the band to the list:
#John Lennon, Paul McCartney, and George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

#step 3: use the for loop and the append() method to prompt the user to 
#add the following members of the band to the list:
#Stu Sutcliffe, and Pete Best;
for i in range(0,1):
    var1=input("please enter Stu Sutcliffe to add it in the list of band: ")
    beatles.append(var1)
    var2=input("please enter Pete Best to add it in the list of band: ")
    beatles.append(var2)
print("Step 3:", beatles)

#step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

#step 5: use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))


# 1. The list is a type of data in Python used to store multiple objects. 
# It is an ordered and mutable collection of comma-separated items between square brackets, e.g.:
my_list = [1, None, True, "I'm String", 256, 0]

# 2. Lists can be indexed and updated, e.g.:
my_list = [1, None, True, "I'm String", 256, 0]
print(my_list[3]) # output I'm String
print(my_list[-1]) # output 0

my_list[1] = '?'
print(my_list) # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

# 3. Lists can be nested, e.g.:
my_list = [1, 'a', ["list", 64, [0, 1], False]]

# 4. List elements and lists can be deleted, e.g.:
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list) # outputs: [1, 2, 4]

del my_list # deletes the whole list

# 5. Lists can be iterated through using the for loop, e.g.:
my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)
    
# 6. The len() function may be used to check the list's length, e.g.:
my_list = ["white", "purple", "blue", "yellow", "green"]
print(len(my_list))  # outputs 5

del my_list[2]
print(len(my_list))  # outputs 4

# 7. A typical function invocation looks as follows: result = function(arg), 
# while a typical method invocation looks like this:result = data.method(arg).