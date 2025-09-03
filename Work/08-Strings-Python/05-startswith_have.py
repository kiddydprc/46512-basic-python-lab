s = input()
s = s.lower() #case insensitive

if len(s) < 4: #too short
    print("NO")
elif s[0:4] == "have": #check first four letters
    print("YES")
else:
    print("NO")
