#6.3
# UMA AJAY KUMAR REDDY P S   19ETCS002134
try:
    x=int(input("enter the numerator"))         #input the valid integer
    y=int(input("enter denominator"))           #input the valid integer
    quo=x/y                 #determinig the quotient
except ValueError as e:     #raising the exception for non integers
    print("invalid input please provide valid one")
except ZeroDivisionError as e:  #exception for division with 0
    print(e)
