# Sequence types and mutability

# What is a tuple?
'''
empty_tuple = ()

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
'''

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

###

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
    

# How to use a tuple: continued
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

###

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


# What is a dictionary?

# How to make a dictionary?
dictionary = {'cat':'chat', 'dog':'chien', 'horse':'cheval'}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary ={}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)


# How to use a dictionary?
print(dictionary['cat'])
print(phone_numbers['Suzy'])

###

dictionary = {'cat':'chat', 'dog':'chien', 'horse':'cheval'}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, 'is not in dictionary')


# Example 1:
dictionary = {
    'cat': 'chat',
    'dog' : 'chien',
    'horse' : 'cheval'
}

# Example 2:
phone_numbers = {
    'boss' : 5551234567,
    'Suzy': 22657854310
}


# How to use a dictionary: the keys()
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

# The sorted() function
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])


# How to use a dictionary: The items() and values() methods
dictionary = {'cat': 'chat', 'dog':'chien', 'horse':'cheval'}

for english, french in dictionary.items():
    print(english, '->', french)
    
###

dictionary = {'cat': 'chat', 'dog':'chien', 'horse':'cheval'}

for french in dictionary.values():
    print(french)
    

# How to use a dictionary: modifying and adding values
dictionary = {'cat': 'chat', 'dog':'chien', 'horse':'cheval'}

dictionary['cat'] = 'minou'
print(dictionary)

# Adding a new key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

###

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({'duck': 'canard'})
print(dictionary)

# Removing a key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)

###

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem() # delete random dictionary
print(dictionary)


# Tuples and dictionaries can work together
school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name] += (score, )
    else:
        school_class[name] = (score, )
    
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)



# Key takeaways: tuples

# 1. Tuples are ordered and unchangeable (immutable) collections of data
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)


# 2. You can create an empty tuple like this:
empty_tuple = ()
print(type(empty_tuple))    # outputs: <class 'tuple'>


# 3. A one-element tuple may be created as follows:
one_elem_tuple_1 = ("one", )    # Brackets and a comma.
one_elem_tuple_2 = "one",       # No brackets, just a comma.

###

my_tuple_1 = 1, 
print(type(my_tuple_1))    # outputs: <class 'tuple'>

my_tuple_2 = 1             # This is not a tuple.
print(type(my_tuple_2))    # outputs: <class 'int'>


# 4. You can access tuple elements by indexing them:
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])    # outputs: [3, 4]


# 5. Tuples are immutable
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple[2] = "guitar"    # The TypeError exception will be raised.

###

my_tuple = 1, 2, 3, 
del my_tuple
print(my_tuple)    # NameError: name 'my_tuple' is not defined


# 6. You can loop through a tuple elements
# Example 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# Example 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# Example 3
tuple_3 = (1, 2, 3, 5)
print(len(tuple_3))

# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)

###

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

###

tup = 1, 2, 3, 
my_list = list(tup)
print(type(my_list))    # outputs: <class 'list'>



# Key takeaways: dictionaries

# 1. Dictionaries are unordered*
'''my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
    }
'''

# 2. If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets (ex. 1)
# or by using the get() method (ex. 2):
pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # outputs: soil

item_2 = pol_eng_dictionary.get("woda")
print(item_2)    # outputs: water


# 3. If you want to change the value associated with a specific key, 
# you can do so by referring to the item's key name in the following way:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]    
print(item)  # outputs: lock


# 4. To add or remove a key (and the associated value), use the following syntax:
phonebook = {}    # an empty dictionary

phonebook["Adam"] = 3456783958    # create/add a key-value pair
print(phonebook)    # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook)    # outputs: {}

###

pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower'}


# 5. You can use the for loop to loop through a dictionary, e.g.:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for item in pol_eng_dictionary:
    print(item) 

# outputs: zamek
#          woda
#          gleba


# 6. If you want to loop through a dictionary's keys and values, you can use the items() method, e.g.:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)


# 7. To check if a given key exists in a dictionary, you can use the in keyword:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

if "zamek" in pol_eng_dictionary:
    print("Yes")
else:
    print("No")


# 8. You can use the del keyword to remove a specific item, or delete a dictionary. 
# To remove all the dictionary's items, you need to use the clear() method:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(len(pol_eng_dictionary))    # outputs: 3
del pol_eng_dictionary["zamek"]    # remove an item
print(len(pol_eng_dictionary))    # outputs: 2

pol_eng_dictionary.clear()   # removes all the items
print(len(pol_eng_dictionary))    # outputs: 0

del pol_eng_dictionary    # removes the dictionary


# 9. To copy a dictionary, use the copy() method:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()
