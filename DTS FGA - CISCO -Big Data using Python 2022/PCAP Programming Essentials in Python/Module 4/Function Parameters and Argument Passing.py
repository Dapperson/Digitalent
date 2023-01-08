# How functions communicate with their environment

# Parameterized functions
'''
def function(parameter):
    ###
'''

###

def message(number):
    print("Enter a number ", number)


# Parametrized functions: continued
def message(number):
    print("Enter a number: ", number)

message(1)

###

def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)
'''
output:
Enter a number: 1
1234
'''

###

def message(what, number):
    print("Enter ", what, " number ", number)
    
###

def message(what, number):
    print("Enter ", what, " number ", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

###

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

###

def introduction (first_name, last_name):
    print("Hello, my name is ", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


# Keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")


#Mixing positional and keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)

###

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3) # option 1

adding(c = 1, a = 2, b = 3) # option 2

adding(3, c = 1, b = 2) # option 3

adding(3, c = 1, b = 2) # option 4

adding(4, 3, c = 2) # option 5


# Parametrized functions - more details
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is ", first_name, last_name)

introduction("James", "Doe") # option 1
# output : Hello, my name is James Doe

introduction("Henry") # option 2
# output : Hello, my name is Henry Smith

introduction(first_name = "William") # option 3
#output : Hello, my name is William Smith

###

def introduction(first_name = "John", last_name="Smith"):
    print("Hello, my name is ", first_name, last_name)

introduction() #option 1
# output : Hello, my name is John Smith

introduction(last_name = "Hopkins") #option 2
# output : Hello, my name is John Hopkins


# Key takeaways
def hi(name):
    print("Hi,", name)

hi("Greg")

###

def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

###

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(s, c, p_c)

###

#Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


#Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

#Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

###

def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3

###

def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
