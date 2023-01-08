# return without an expression

'''
def function():
    return expression
'''

def happy_new_year (wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

# happy_new_year()

happy_new_year(False)


def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)


def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")


# A few words about None
value = None
if value is None:
    print("Sorry, you don't carry any value")
    
# A few words about None: continued
def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))


# Effects and results: lists and functions
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([5, 4, 3]))


# Effects and results: lists and functions - continued
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
        
    return strange_list

print(strange_list_fun(5))


###


def leap_year(year):
    if year % 400 == 0:
        print(year , "is a leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print(year , "is a leap year")
    else:
        print(year, "is NOT a leap year")

year = int(input("Please Enter a year: "))
leap_year(year)

def is_year_leap(year):
    if year == 2000 or year == 2016:
        return True
    else:
        return False

test_data = [1900 , 2000 , 2016 , 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


###


def is_year_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 100:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if year < 1989 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    rsday = days[month-1]
    if month == 2 and is_year_leap(year):
        rsday = 29
    return rsday

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


###


def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res

def day_of_year(year, month, day):
	days = 0
	for m in range(1, month):
		md = days_in_month(year, m)
		if md == None:
			return None
		days += md
	md = days_in_month(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(day_of_year(2000, 12, 31))


###

# prime numbers
def is_prime(num):
    div = 2
    while div < num:
        if num % div == 0:
            return False
        div += 1
    return True
            
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()



###


def liters_100km_to_miles_gallon(liters):
    gallon = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallon
    
def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    liters = 3.785411784
    return liters / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


#Key takeaways
def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None

###

def wishes():
    return "Happy Birthday!"

w = wishes()

print(w)    # outputs: Happy Birthday!

###

# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes


# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

# outputs: My Wishes
#          Happy Birthday

###

def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)

hi_everybody(["Adam", "John", "Lucy"])

###

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

