#6.8.1: Nested loops: Print rectangle
#Given the number of rows and the number of columns, write nested loops to print a rectangle.

#Sample output with inputs: 2 3
#* * * 
#* * * 

num_rows = int(input())
num_cols = int(input())

num_rows += 1
    
for num_rows in range(1, num_rows, 1):
    print('*', end=' ')
    for num_cols in range(1, num_cols, 1):
        num_cols += 1

        print('*', end=' ')
    print()

