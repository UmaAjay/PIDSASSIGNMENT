#2.4
#UMA AJAY KUMAR REDDY P S   19ETCS002134
s={1,2,3,4,5,5}         #creating a new set
s.add(6)                # adding new item to a set
print("set s: ",s)
s2=s.copy()            #a copy of the set s assigned to a set s2
print("copied set s2: ",s2)

s3={2,3,4}              #creating a new set
s2=s2-s3                #Removing the items in the set s2 that are also included in the set s3
print("updated set after removing items: ",s2)      #now s2 will be {1,5,6}

s.remove(2)             #Removing item 2 from set s
print("set s after removing item 2: ",s)


s4=s.intersection(s3)               #Returning a set that is the intersection of two sets
print("intersection set of sets s and s3: ",s4)

print("symmetric difference of sets s and s3: ",s.symmetric_difference(s3))
                                                        #symmetric differences of two sets

print("the union of two sets s and s3: ",s.union(s3))



