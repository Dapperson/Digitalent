# Functions and scopes
def scope_test():
    x = 123

scope_test()


# Functions and scopes: continued
def my_function():
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)


# Functions and scopes: the global keyword
def my_function():
    global var
    var = 2
    print("Do I know that function?", var)

var = 1
my_function()
print(var)


# How the function interacts with its arguments
def my_function(my_list_1):
    print("Print #1: ", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
    
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

###

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

###

def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)

var = 1
my_function(var)
print(var)


# Key takeaways

var = 2

def mult_by_var(x):
    return x * var

print(mult_by_var(7)) # output: 14


###


def mult(x):
    var = 5
    return x * var

print(mult(7))  # output: 35


###


def mult(x):
    var = 7
    return x * var

var = 3
print(mult(7)) # output: 49


###


def adding(x):
    var = 7
    return x + var

print(adding(4))    # output:   11
print(var)  # NameError


###


var = 2
print(var)  # output: 2

def return_var():
    global var
    var = 5
    return var

print(return_var()) # output: 5
print(var)  # output: 5