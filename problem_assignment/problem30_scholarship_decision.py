# 30. Complete Scholarship Decision

age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

if age < 18 or age > 25 or marks < 85 or attendance < 75 or income > 300000:
    print("Scholarship Rejected")
    if age < 18 or age > 25:
        print("Reason: Age must be between 18 and 25")
    if marks < 85:
        print("Reason: Marks below 85")
    if attendance < 75:
        print("Reason: Attendance below 75%")
    if income > 300000:
        print("Reason: Family income above 300000")
else:
    print("Scholarship Approved")
