#3.2
# UMA AJAY KUMAR REDDY P S   19ETCS002134
dict={"Kiranraj":"Charlie777","Prashanth":"KGF","Rajamouli":"RRR"}     #creating a new dictionary
L=list(dict.keys())                                          #return a list containing the dictionary's keys
print("returning a list containing the dictionary's keys",L,"\n")
dict.pop("Rajamouli")                                       #removing the element with the specified key
print("after removing the the element with the specified key ",dict,"\n")

dict.popitem()                                              #Removing the last inserted key-value pair
print("Removing the last inserted key-value pair",dict,"\n")

dict2={"Vetrimaaran":"Vada Chennai","Rishab":"Kantara"}      #creating a new dictionary

dict.update(dict2)                                          # Update the dictionary with the specified key-value pairs
print("Updated dictionary with the specified key-value pairs",dict,"\n")

L2=list(dict.values())                                      #Returning a list of all the values in the dictionary
print("Returning a list of all the values in the dictionary",L2,"\n")

dict.pop("Kiranraj")                                       #removing the element with the specified key
print("after removing the element with the specified key ",dict,"\n")