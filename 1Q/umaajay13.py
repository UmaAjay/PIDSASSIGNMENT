#1.3
#UMA AJAY KUMAR REDDY P S   19ETCS002134

L=list([1,2,3,4,5,5] )            # creating a new list
L.append(6)                 # Adding an element at the end of the list
L2=L                        # copying list L to list L2
print("copied list L2: ",L2)                   # Returning a copy of the list
print("number of times of occurance of element 5: ",L2.count(5))
                            # counting number of times of occurance of element 5
L3=[7,8,9]                  # creating a new list
L.extend(L3)                # Adding the elements of a list, to the end of the current list
print("after adding the elements of a list, to the end of the current list L: ",L)

print("Returning the index of the first element with the value 5: ", L.index(5))
                #Returning the index of the first element with the specified value

L.insert(6,6)           #Adding an element at the specified position
print("after adding 6 at index 6 : ",L,"\n")
L.pop(6)                # after removing an element at the specified position
print("after removing 6 at index 6 : ",L,"\n")

L.remove(8)             # removing the element 8 by specifying the value
print("after removing the element 8 by specifying the value",L,"\n")


L.reverse()             #Reversing the order of the list
print("after reversing the order of the list L: ",L,"\n")
