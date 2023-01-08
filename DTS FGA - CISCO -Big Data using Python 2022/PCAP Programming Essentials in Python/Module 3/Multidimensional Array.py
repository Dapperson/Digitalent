#Lists in lists
'''
row = []
for i in range(8):
    row.append(WHITE_PAWN)

row = [WHITE_PAWN for i in range(8)]
'''

squares = [x ** 2 for x in range(10)]

twos = [2 ** i for i in range(8)]

odds = [x for x in squares if x % 2 != 0]

# Lists in lists: two-dimensional arrays
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

###

board = [[EMPTY for i in range(8) for j in range(8)]] 


# Lists in lists: two-dimensional arrays - continued
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)


# Multidimensional nature of lists: advanced applications

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here
#

total = 0.0

for day in temps:
    total += day[11]
    
average = total / 31

print("Average temperature at noon:", average)

###

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
print("The highest temperature was:", highest)

###

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot")


# Three-dimensional arrays
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
rooms[0][4][1] = False

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
        

# Key takeaways
# 1. List comprehension
'''
[expression for element in list if conditional]

for element in list:
    if conditional:
        expression
'''

cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]

# 2. nested lists matices
# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

###

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'