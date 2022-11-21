#6.1
# UMA AJAY KUMAR REDDY P S   19ETCS002134
import functools
import operator
num=(10,11,12,13,14,16)           #numbers whose square to be found
print("the list of numbers are: ",num)
res=map(lambda y:y**2, num)         #using map and lambda to find squares.
print("the obtained squares using map are: ",list(res))
res2=filter(lambda z: z% 2!=0,num)  # usinf filter to know the odd numbers
print("the odd number among given numbers are: ",list(res2))
print("summation of all numbers in num using reduce: ",functools.reduce(operator.add,num)) # using reduce to find sum of all elements of num