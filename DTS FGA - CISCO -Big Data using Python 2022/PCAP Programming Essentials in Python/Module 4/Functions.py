#Your first function
print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())

###

'''
def function_name():
    function_body
'''

###

def message():
    print("Enter a value: ")

print("We start here.")
print("We end here.")

###

def message():
    print("Enter a value: ")

print("We start here.")
message()
print("We end here.")


# Functions
print("We start here")

def message():
    print("Enter a value")

message()
a = int(input())

message()
b = int(input())

message()
c = int(input())

print("We end here")


# Key takeaways
'''
def your_function(optional parameters):
    # the body of the function
'''

###

def message():    # defining a function
    print("Hello")    # body of the function

message()    # calling the function

###

def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function