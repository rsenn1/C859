#10.7.1: LAB: Count characters
#Write a program whose input is a string which contains a character and a phrase, and #whose output indicates the number of times the character appears in the phrase.
#Ex: If the input is:
#n Monday
#the output is:
#1

phrase = input()
phrase = (phrase.split())
character = phrase[0]
phrase = ' '.join(phrase[1:])
print(phrase.count(character))
