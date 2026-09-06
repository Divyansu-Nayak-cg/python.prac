# E. Multiple Conditions - Q23. Allowed when age >= 18 and has_id is True
age = int(input("Enter age: "))
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"
if age >= 18 and has_id is True:
    print("Allowed")
