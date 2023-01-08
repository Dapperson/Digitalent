# AND, OR, NOT
var = 1
# Example 1:
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))


not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)


i = 1
j = not not i


# Bitwise
'''
& (ampersand) - bitwise conjunction;
| (bar) - bitwise disjunction;
~ (tilde) - bitwise negation;
^ (caret) - bitwise exclusive or (xor).
'''

'''
Each of these two-argument operators can be used in abbreviated form. 
These are the examples of their equivalent notations:

x = x & y	x &= y
x = x | y	x |= y
x = x ^ y	x ^= y
'''

#Exercise 1
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))


#Exercise 2
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)