#zyDE 7.5.1: Temperature conversion.
#Complete the program by writing and calling a function that 
#converts a temperature from Celsius into Fahrenheit. 
#Use the formula F = C x 9/5 + 32. 
#Test your program knowing that 50 Celsius is 122 Fahrenheit.

def c_to_f(temp_c, temp_f):
    return  temp_f

temp_c = float(input('Enter temperature in Celsius: '))
print()
temp_f = None

temp_f = (temp_c * 9) / 5 + 32

print('Fahrenheit:' , temp_f)
