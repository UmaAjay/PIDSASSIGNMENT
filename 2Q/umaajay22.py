#2.2
#UMA AJAY KUMAR REDDY P S   19ETCS002134
tup=tuple((1,2,3,4,5,5))                # #creating a new tuple
i=0                                     # initializing counter i to 0
while i<len(tup):                       # a while loop to go through all the index numbers
    print("At index: ", i, " the element is ", tup[i])
    i+=1                                # incrementing i value at every iteration


tup2=(6,7)                              #creating a new tuple
tup3=tup+tup2                           #Joining two tuples using the + operator
print("tup + tup2 = ",tup3)


print("multiply the content of a tuple",tup3*2)


