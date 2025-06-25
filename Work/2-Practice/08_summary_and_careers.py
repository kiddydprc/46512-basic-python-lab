#input
bill, tip_percent, people = map(float, input().split())
people = int(people)

# Calculate
tip_amount = bill * tip_percent / 100
total = bill + tip_amount
per_person = total / people

# Output
print("Each person pays: ", round(per_person, 2))

# Python careers: Data Analyst, AI Engineer, Web Developer, etc.