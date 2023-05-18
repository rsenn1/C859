#6.14 LAB: Convert to binary (in reverse)
#Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in binary. 

user_input = input()
x = int(user_input)
while x > 0:
    y = (x % 2)
    x //= 2
    print(int(y), end='')
