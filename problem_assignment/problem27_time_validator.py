# 27. Time Validator

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if hours < 0 or hours > 23:
    print("Invalid time")
elif minutes < 0 or minutes > 59:
    print("Invalid time")
elif seconds < 0 or seconds > 59:
    print("Invalid time")
else:
    print("Valid time")
