#6.15 LAB: Password modifier
#Many user-created passwords are simple and easy to guess. 
#Write a program that takes a simple password and makes it stronger by replacing characters using the key below, 
#and by appending "!" to the end of the input string.

#i becomes 1
#a becomes @
#m becomes M
#B becomes 8
#s becomes $

word = input()
password = ''

password = word.replace("i", "1" )
password = password.replace("a", "@" )
password = password.replace("m", "M")
password = password.replace("B", "8" )
password = password.replace("s", "$" )

print('{}!'.format(password))
