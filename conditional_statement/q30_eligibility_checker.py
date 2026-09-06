# F. Combining Conditions - Q30. Eligibility Checker
# Eligible only when age >= 18 and marks >= 40 and has_id is True
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"

if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")

# Why 'and' is appropriate:
# 'and' requires ALL conditions to be True. Here eligibility needs
# age, marks, AND id together. If any one fails, the person must
# not be eligible, so 'or' would be wrong because 'or' passes
# when just one condition is True.
