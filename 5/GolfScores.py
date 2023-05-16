#Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies from hole to hole and is called par (i.e. 3, 4, or 5). 
#Each score's name is based on the actual strokes taken compared to par:

#"Eagle": number of strokes is two less than par
#"Birdie": number of strokes is one less than par
#"Par": number of strokes equals par
#"Bogey": number of strokes is one more than par
#Given two integers that represent par and the number of strokes used, write a program that prints the appropriate score name. Print "Error" if par is not 3, 4, or 5.

list = [3, 4, 5]
par = int(input())
strokes = int(input())
if par not in list:
   print("Error")
elif (strokes + 2) == par:
    print("Eagle")
elif (strokes + 1) == par:
    print("Birdie")
elif strokes == par:
   print("Par")
elif (strokes - 1) == par:
   print("Bogey")
