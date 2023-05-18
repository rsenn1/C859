#6.16 LAB: Brute force equation solver
#Numerous engineering and scientific applications require finding solutions to a set of equations. 
#Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2. 
#Given integer coefficients of two linear equations with variables x and y,
#use brute force to find an integer solution for x and y in the range -10 to 10.

# Read in first equation, ax + by = c 
# Read in second equation, dx + ey = f 

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

found_solution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if (x == (c - b*y) / a) and  (y == (f - d*x) / e):
            print('x = {} , y = {}'.format(x,y))
            found_solution = True
if not found_solution:
    print("There is no solution")
    
