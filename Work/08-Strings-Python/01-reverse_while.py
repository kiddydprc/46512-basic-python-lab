s = input()
st = len(s) - 1 #the last letter position
n = ""

while st >= 0: #print from behind
    n += s[st]
    st -= 1

print(n)