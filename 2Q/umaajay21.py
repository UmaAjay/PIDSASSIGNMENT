#2.1
#UMA AJAY KUMAR REDDY P S   19ETCS002134

tup=tuple((1,2,3,4,5,5))                # creating a new tuple(it contains duplicate items too)

L=list(tup)                             # Converting the created tuple into a list
print("tuple converted to list",L)                                # tuple converted to list
for i in range(len(tup)):   # Looping through the tuple items by referring to their index number
    print("At index: ",i," the element is ",tup[i])


    