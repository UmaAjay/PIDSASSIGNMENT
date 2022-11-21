#5.4
# UMA AJAY KUMAR REDDY P S   19ETCS002134
s="Malayalam"               # given string
r="%"                       # second character have to be changed to '%'
repl=s[:2]+s[2:].replace(s[1],r)        # second character have been changed to '%',except the second character itself
print("replaced string: ",repl)
