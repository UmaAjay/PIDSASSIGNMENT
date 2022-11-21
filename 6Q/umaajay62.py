#6.2
# UMA AJAY KUMAR REDDY P S   19ETCS002134

f=open("hey.txt","w")     #creating a file
f.write("Pids assignment")
f.close()  # closing file

f=open("hey.txt","r")
print(f.read())
f.close()
f=open("hey.txt", "a")
f.write(" I am adding contents at the end of the file")  # appends to end
f.close()
f = open("hey.txt")
print(f.read())
f.close()
f=open("hey.txt", "w")  # overurites the fite
f.write("previous part is overwritten")
f.close()
f=open("hey.txt","r")           #reading file
print(f.read())
f.close()
f = open("hey.txt","x")          #Binory mode