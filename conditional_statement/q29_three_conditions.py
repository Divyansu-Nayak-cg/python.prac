# F. Combining Conditions - Q29. Allowed only when all three are True
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"
has_ticket = input("Do you have ticket? (yes/no): ").lower() == "yes"
if is_student and has_id and has_ticket:
    print("Allowed")
else:
    print("Not allowed")
