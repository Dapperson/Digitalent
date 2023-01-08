'''
nama Varibel tidak bisa menggunaka keywords
berikut nama-nama keywords

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 
'except', 'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
print()

var = "3.8.5"
print("Python version: " + var)
print()

var = 1
print(var)
var = var + 1
print(var)
print()

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
print()

john = 4
mary = 4
adam = 4
total_apples = john + mary + adam
print("Total number of apples:",total_apples)
print()

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
print()

x =  1
x = float(x)
y = (3*(x**3)) - (2*(x**2)) + (3*x) - 1
print("y =", y)
print()

var = 2
print(var)

var = 3
print(var)

var += 1
print(var)
print()