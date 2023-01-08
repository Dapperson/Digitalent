# black_sheep == 2 * white_sheep
# black_sheep == (2 * white_sheep)

var = 0 #Assigning 0 to var
print(var == 0)

var = 1 #Assigning 1 to var
print(var == 0)

var = 0 #Assigning 0 to var
print(var != 0)

var = 1 #Assigning 1 to var
print(var != 0)
print()

'''
Priority	Operator	
1	+, -	unary
2	**	
3	*, /, //, %	
4	+, -	binary
5	<, <=, >, >=	
6	==, !=
'''

n = float(input("Masukkan angka: "))

if n <= 100:
    print("Nilai n kurang dari 100 : ", n <= 100)
else:
    print("Nilai n kurang dari 100 : ", n <= 100)
print()


#Analyzing code samples
#Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

#We temporally assume that the first number is the largest one
#We will verifiy this soon
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2
    
# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

#Print the result
print("The larger number is: ", largest_number)
print()


word = input("Please enter the word Spathiphyllium: ")

upperWord = "Spathiphyllium"
lowerWord = "spathiphyllium"

if word == upperWord:
    print("Yes - Spathiphyllum is the best plant ever!")
elif word == lowerWord:
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", word+ "!")
print()


income = float(input("Enter the annual income: "))

if income < 85_528:
    tax = (income * .18) - 556.2
    if tax < 0:
        tax = 0
else:
    tax = ((income - 85_528)* 0.32) + 14_839.2

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
print()


year = int(input("Enter a year: "))

if year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")
print()


# Key takeaways

# The Comparison
x = 0
y = 1
z = 0

x == y #False
x == z #True

x != y #True
x != z #False

x > y #False
y > z #True

x < y #True
y < z #False

x >= y  # False
x >= z  # True
y >= z  # True

x <= y  # True
x <= z  # True
y <= z  # False

# Conditional Statement

# a single if statement
x = 10

if x == 10: # condition
    print('x is equal to 10') # Executed if the condition is True
    
#a series of if statements
x = 10

if x > 5: # condition one
    print("x is greater than 5") # Executed if condition one is True
if x < 10: # condition two
    print("x is less than 10") # Executed if condition one is True
if x == 10: # condition three
    print("x is equal to 10") # Executed if condition one is True

# an if-else statement
x = 10

if x < 10: # condition
    print("x is less than 10") # Executed if condition one is True
else:
    print("x is greater than or equal to 10") # Executed if condition one is False
    
# a series of if statements followed by an else
x = 10

if x > 5: # True
    print("x > 5")
if x > 8: # True
    print("x > 8")
if x > 10: # False
    print("x > 10")
else:
    print("else will be executed")
    
# The if-elif-else statement
x = 10

if x == 10: # True
    print("x == 10")
if x > 15: # Flase
    print("x > 15")
elif x > 10: # False
    print("x > 10")
elif x > 5: #True
    print("x > 5")
else:
    print("else will not be exeuted")
    
# Nested conditional statements
x = 10

if x > 5: # True
    if x == 6: # False
        print("nested: x == 6")
    elif x == 10: #True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")