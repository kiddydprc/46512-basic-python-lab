age = int(input()) #get age
day = int(input()) #get day

#set the price for each age group
if age < 13:
    price = 100
elif age <= 60:
    price = 180
else:
    price = 120


#check if it weekend
if day in [6, 7]:
    price += 50


print(price) #output
