#4.3
# UMA AJAY KUMAR REDDY P S   19ETCS002134
print("all prime numbers from 50 to 100")
for i in range(50,101):               # looping to get all prime numbers from 50 to100
    count=0
    for j in range(2,(i//2+1)):
        if i%j==0:
            count=1
            break
        else:
            continue
    if count==0:
        print("{}".format(i))
