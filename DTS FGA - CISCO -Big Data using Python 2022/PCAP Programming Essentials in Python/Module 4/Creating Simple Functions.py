# Some simple functions: evaluating the BMI
def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))


# Some simple functions: evaluating BMI and converting imperial units to metric units

# convert imperial units to metric ones
def lb_to_kg(lb):
    return lb * 0.45359237

print(lb_to_kg(1))

###

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1))

###

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))
print(bmi(352.5, 1.65))


# Some simple functions: continued

# three parameters
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

###

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Some simple functions: triangles and the Pythagorean theorem

# right-angle triangle.
# Pythagorean theorem: c^2 = a^2 + b^2
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

###

def is_a_triangle():
    return a + b > c and b + c > a and c + a > b

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')
    
    
# Some simple functions: evaluating a triangle's area
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

print(area_of_triangle(1., 1., 2. ** .5))


###


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')
    

# Some simple functions: factorials
'''
0! = 1 (yes! it's true)
1! = 1
2! = 1 * 2
3! = 1 * 2 * 3
4! = 1 * 2 * 3 * 4
:
:
n! = 1 * 2 ** 3 * 4 * ... * n-1 * n
'''

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6): #testing
    print(n, factorial_function(n))
    

# Some simple functions: Fibonacci numbers
'''
fib_1 = 1
fib_2 = 1
fib_3 = 1 + 1 = 2
fib_4 = 1 + 2 = 3
fib_5 = 2 + 3 = 5
fib_6 = 3 + 5 = 8
fib_7 = 5 + 8 = 13
'''

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10): #testing
    print(n, "->", fib(n))
    

# Some simple functions: recursion

# The Fibonacci numbers definition is a clear example of recursion
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

# The factorial has a second, recursive side too
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)


# Key takeaways

# Recursive implementation of the factorial function.
def factorial(n):
    if n == 1: # The base case (termination condition)
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(4)) # 4 * 3 * 2 * 1 =24