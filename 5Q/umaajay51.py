#5.1

s="Python"                      # string creation
s[0]="M"                        # gives error because strings are immutable
s.pop()                          # gives error because strings are immutable


print("string s: ",s)
print("accessing one specific character from a string:  ",s[2])

s2=" for data science"           # string creation
s3=s+s2                         # Concatenating 2 strings
print("concatenated string: ",s3)


for i in range(len(s)):             # iteration through a string s
    print("character at index",i, " is ",s[i])
