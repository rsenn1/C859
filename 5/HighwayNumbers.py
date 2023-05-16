#5.14 LAB: Interstate highway numbers

#Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. 
#Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. 
#Thus, I-405 services I-5, and I-290 services I-90.

#Given a highway number, indicate whether it is a primary or auxiliary highway. 
#If auxiliary, indicate what primary highway it serves. 
#Also indicate if the (primary) highway runs north/south or east/west.

highway_number = int(input())

if (1 > highway_number > 199) or (highway_number % 100 == 0):
    print(highway_number, "is not a valid interstate highway number.")
else:
    if (highway_number > 0) and (highway_number < 100):
        print("I-",end='')
        print(highway_number,"is primary, ",end= '')
    if 99 < highway_number < 1000:
        print("I-",end='')
        print(highway_number,end=' ')
        print("is auxiliary, serving I-",end='')
        print(int(str(highway_number)[-2:]),end='')
        print(",",end=' ')
    if highway_number % 2 == 0:
        print("going east/west", end= '')
    else:
        print("going north/south", end= '')
    print(".")
