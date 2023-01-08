#Bila input yg ditulis tidak enggunakan keterangan variabel, maka otomatis bertipe string

print("Tell  me anything...")
anything = input()
print("Hmm...", anything, "... Really?")
print()

anything = float(input("Enter a number:"))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
print()

leg_a = float(input("Input first leg lenght:"))
leg_b = float(input("Input second leg length:"))
hypo = (leg_a**2 + leg_b**2) ** 0.5
print("Hypotenuse length is", hypo)
print()

fnam = input("Can I have your first name, please? ")
lnam = input("Can I have your last name, please? ")
print("Thank you")
print("\nYour name is " + fnam + " " + lnam + ".")
print()

print("+" + 10 * "-" + "+")
print(("|" + 10 * " " + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
print()

leg_a = float(input("Input first leg lenght:"))
leg_b = float(input("Input second leg length:"))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** 0.5))
print()

# input a float value for variable a here
a = float(input("Input first float number: "))
# input a float value for variable b here
b = float(input("Input second float number: "))

# output the result of addition here
print(a + b)
# output the result of subtraction here
print(a - b)
# output the result of multiplication here
print(a * b)
# output the result of division here
print(a / b)

print("\nThat's all, folks!")
print()

x = float(input("Enter value for x: "))
y = 1/(x+1/(x+1/(x+1/x)))
print("y =", y)
print()

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
durationhours = dura/60+hour
minutes = (mins + dura) %60
hours = int(hour + (mins +dura) / 60) % 24
print(hours,":",minutes,sep="")
print()
'''
Sample input:
23
58
642

Expected output: 10:40
'''

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")
print()

x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")
print()

x = input("Enter a number: ") # The user enters 2
print(type(x))
print()