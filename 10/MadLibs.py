#10.8 LAB: Mad Lib - loops
#Mad Libs are activities that have a person provide various words, which are then used to #complete a short story in unexpected (and hopefully funny) ways.
#Write a program that takes a string and an integer as input, and outputs a sentence using #the input values as shown in the example below. The program repeats until the input  #string is quit and disregards the integer input that follows.

while True:
    phrase = input()
    if 'quit' in phrase:
        break
    phrase = (phrase.split())
    number = phrase[1]
    word = phrase[0]
    phase = ' '.join(phrase[1:])
    print('Eating {} {} a day keeps the doctor away.'.format(number, word))
