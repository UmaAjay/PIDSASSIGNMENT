#2.3
#UMA AJAY KUMAR REDDY P S   19ETCS002134
s=set((2,5,7,9,4,2,1,6))         # Create a set of items using set() constructor
print("set s :",s)              # output will be unordered and there will be no duplicates

# s[0]=5                          # sets are unchangable so gives error

L=[1,2,3,3,2]                   # creating a list
s2=frozenset(L)                 #frozenset() Method  creates an immutable Set object from an iterable
print("frozenset s2: ",s2)
#s2.add(5)                       # gives error because frozenset() Method is immutable




