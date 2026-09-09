# 10. Voting Eligibility

age = int(input("Enter age: "))

if age < 0 or age > 120:
    print("Invalid age")
elif age >= 18:
    print("Can vote")
else:
    print("Cannot vote")
