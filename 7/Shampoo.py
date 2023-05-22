#7.7.3: Function with loop: Shampoo.
#Write a function print_shampoo_instructions() with parameter num_cycles. 
#If num_cycles is less than 1, print "Too few.". If more than 4, print "Too many.". 
#Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number, 
#followed by "Done.".

#Sample output with input: 2
#1 : Lather and rinse.
#2 : Lather and rinse.
#Done.


def print_shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print("Too few.")
    elif num_cycles > 4:
        print("Too many.")
    else:
        count = 1
        while count <= num_cycles:
            print(count, ": Lather and rinse.")
            count += 1
        print("Done.")

user_cycles = int(input())
print_shampoo_instructions(user_cycles)
 
