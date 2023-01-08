#Looping Code with WHILE

'''
while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n
'''

''' while True:
     print("I'm stuck inside a loop")'''
    
#To terminate your program, just press Ctrl-C (or Ctrl-Break on some computers)


#Store the current largest number here
largest_number = -999_999_999

#input the first value
number = int(input("Enter a number or type -1 to stop: "))

#if the number is not equal to -1, continue
while number != -1:
    #Is number larger than largest_number?
    if number > largest_number:
        #Yes, update largest_number
        largest_number = number
    #Input the next number
    number = int(input("Enter a number or type -1 to stop: "))

#Print the largest number
print("The largest number is ", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


#Guess the secret number

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = 0

while number != secret_number:
    number = int(input("input the secret number: "))
    if number == secret_number:
        print("Well done, muggle! You are free now.")
    else:
        print("Ha ha! You're stuck in my loop!")


# Looping your code with FOR

for i in range(100):
    #do something
    pass

for i in range(10):
    print("The value of i is currently,", i)
    
for i in range(2, 8):
    print("The value of i is currently,", i)
    

# There will be no output:
for i in range (1, 1):
    print("The value of i is currently", i)
    
for i in range(2, 1):
    print("The value of i is currently", i)

    
power = 1
for expo in range(16):
    print("2 to the power of ", expo, " is", power)
    power *= 2 

for i in range(2, 8, 3):
    print("The value of i is currently", i)


#counting mississippily

import time

# Write a for loop that counts to five.
for i in range(1, 6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)

# Write a print function with the final message.
print("Ready or not, here I come!")


#The break and continue statements

#break example
print("The break instruction")
for i in range(1, 6):
    if i == 3:
        break
    print("inside the loop ", i)
print("outside the loop ", i)

#continue example
print("The continue instruction")
for i in range(1, 6):
    if i == 3:
        continue
    print("inside the loop ", i)
print("outside the loop ", i)


# The break and continue statements: more examples
largest_number = -999_999_999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is ", largest_number)
else:
    print("You haven't entered any number")


largest_number = -999_999_999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1
    
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is ", largest_number)
else:
    print("You haven't entered any number")
    

#Stuck in a loop
secret_word = "chupacabra"

while True:
    name = input("Enter secret word to leave the loop: ")
    if name == secret_word:
        print("You've successfully left the loop.")
        break
    else:
        print("Your stuck in an infinite loop")


#the Ugly Vowel Eater
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else: 
        print(letter, end="\n")


#the Pretty Vowel Eater
word_without_vowels = ""

user_word = input("Enter a word: ")
user_word = user_word.upper()

for i in user_word:
    if i in ("AIUEO"):
        continue
    word_without_vowels += i
print(word_without_vowels)


#else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else: ", i)


for i in range(5):
    print(i)
else:
    print("else:", i)


i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)


#Essentials of the while loop
blocks = int(input("Enter the blocks : "))

height = 0
layers = 1

while layers <= blocks:
    height += 1
    blocks -= layers
    layers += 1
print("The height of the pyramid: ", height)


#Collatz's hypothesis
c0 = int(input("Enter a number: "))

steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0/2)
        print(c0)
    else:
        c0 = int(3 * c0 + 1)
        print(c0)
        
    steps += 1

print("steps = ", steps)


#Key takeaways
# Example 1
'''while True:
    print("Stuck in an infinite loop.")'''

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1


# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)


text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")


text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")


n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")


for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

