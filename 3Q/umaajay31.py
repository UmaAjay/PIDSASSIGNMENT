# 3.1
# UMA AJAY KUMAR REDDY P S   19ETCS002134
dict={"Kiranraj":"Charlie777","Prashanth":"KGF","Rajamouli":"RRR","Prashanth":"KGF"}     #creating a new
                                                                # dictionary(it does not allow duplicates)
print("dictionary dict: ",dict)                             #we can see that it is ordered

dict["Rajamouli"]="Bahubali"                                    #dictionaries are changeable/mutable
print("after changing the value of the key 'Rajamouli' \n",dict)

print("Returning a dictionary with the specified keys and value :",{"Kiranraj":dict["Kiranraj"]})

print("Returning the value of the specified key: ",dict["Kiranraj"])

key="Nelson"                                        #let specified key be "Nelson"
if key in dict.keys():                              #
    print("Returning the value of the specified key: ",dict[key])
else:                                       #If the key does not exist: insert the key, with the specified value
    dict[key]="Doctor"
print("dictionary dict: ",dict)

L=[]                                    # creating new list
for i in dict.keys():                   # looping to get each key value pair
    t=(i,dict[i])                       # creating a tuple which has key value pair
    L.append(t)                         # appending tuple which has key value pair
print("Returning a list containing a tuple for each key value pair. ",L)
