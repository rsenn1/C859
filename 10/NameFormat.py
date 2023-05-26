#10.6 LAB: Name format
#Many documents use a specific format for a person's name. Write a program whose input is:
#firstName middleName lastName and whose output is: lastName, firstInitial.middleInitial.
#Ex: If the input is:
#Pat Silly Doe
#the output is:
#Doe, P.S.

input_name = input()
name_list = (input_name.split())

if len(name_list) > 2:
    last = name_list[2]
    first = name_list[0]
    middle = name_list[1]
    print('{}, {}.{}.'.format(last, first[:1],middle[:1]))

else:
    last = name_list[1]
    first = name_list[0]
    print('{}, {}.'.format(last, first[:1]))
    

