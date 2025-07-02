num=float(input()) #input price

#calculate discount
if num>=2000:
    dis=0.85
elif num>=1000:
    dis=0.9
elif num>=500:
    dis=0.95
else: dis=1

print(num*dis) #opt