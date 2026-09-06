# 09 - Conditionals - All Questions (Q1-Q30 combined)
# Source folder: conditional_statement/
# Each section below is copied verbatim from its original q*.py file

# ============================================================
# Q1 - from q1_greater_than_10.py
# ============================================================
# A. Basic if - Q1. Check whether a number is greater than 10
number = int(input("Enter a number: "))
if number > 10:
    print("Greater than 10")

# ============================================================
# Q2 - from q2_adult_check.py
# ============================================================
# A. Basic if - Q2. Check whether a person's age is at least 18
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")

# ============================================================
# Q3 - from q3_positive_check.py
# ============================================================
# A. Basic if - Q3. Print Positive if number is greater than 0
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")

# ============================================================
# Q4 - from q4_pass_check.py
# ============================================================
# A. Basic if - Q4. Check marks >= 40 and print Pass
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")

# ============================================================
# Q5 - from q5_zero_check.py
# ============================================================
# A. Basic if - Q5. Print Zero when number is equal to 0
number = int(input("Enter a number: "))
if number == 0:
    print("Zero")

# ============================================================
# Q6 - from q6_positive_or_not.py
# ============================================================
# B. if-else - Q6. Check whether a number is positive or not
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
else:
    print("Not positive")

# ============================================================
# Q7 - from q7_adult_or_minor.py
# ============================================================
# B. if-else - Q7. Display Adult if age >= 18, otherwise Minor
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# ============================================================
# Q8 - from q8_even_or_odd.py
# ============================================================
# B. if-else - Q8. Check whether a number is even or odd using %
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

    

# ============================================================
# Q9 - from q9_pass_or_fail.py
# ============================================================
# B. if-else - Q9. Display Pass if marks >= 40, otherwise Fail
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# ============================================================
# Q10 - from q10_greater_of_two.py
# ============================================================
# B. if-else - Q10. Take two numbers and print which one is greater
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")

# ============================================================
# Q11 - from q11_grades.py
# ============================================================
# C. if-elif-else - Q11. Grade system: A, B, C, D, F
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

# ============================================================
# Q12 - from q12_positive_negative_zero.py
# ============================================================
# C. if-elif-else - Q12. Display Positive, Negative, Zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# ============================================================
# Q13 - from q13_day_name.py
# ============================================================
# C. if-elif-else - Q13. Day number to day name (1-5)
day = int(input("Enter day number (1-5): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Other")

# ============================================================
# Q14 - from q14_excellent_good_pass_fail.py
# ============================================================
# C. if-elif-else - Q14. Excellent, Good, Pass, Fail using ranges
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

# ============================================================
# Q15 - from q15_one_two_three.py
# ============================================================
# C. if-elif-else - Q15. Display 1, 2, 3 or Other
number = int(input("Enter a number: "))
if number == 1:
    print("1")
elif number == 2:
    print("2")
elif number == 3:
    print("3")
else:
    print("Other")

# ============================================================
# Q16 - from q16_between_18_and_60.py
# ============================================================
# D. Nested Conditions - Q16. Check 18 to 60
age = int(input("Enter your age: "))
if age >= 18:
    if age <= 60:
        print("Between 18 and 60")

# ============================================================
# Q17 - from q17_nested_pass_good.py
# ============================================================
# D. Nested Conditions - Q17. Passed -> Good / Passed, else Failed
marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 75:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")

# ============================================================
# Q18 - from q18_nested_positive_100.py
# ============================================================
# D. Nested Conditions - Q18. Positive, then greater than 100
number = int(input("Enter a number: "))
if number > 0:
    if number > 100:
        print("Positive and greater than 100")
    else:
        print("Positive but not greater than 100")
else:
    print("Not positive")

# ============================================================
# Q19 - from q19_nested_age.py
# ============================================================
# D. Nested Conditions - Q19. Age >= 18, then >= 60
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 60:
        print("Senior adult")
    else:
        print("Adult")
else:
    print("Minor")

# ============================================================
# Q20 - from q20_nested_nonzero.py
# ============================================================
# D. Nested Conditions - Q20. Non-zero, then positive or negative
number = int(input("Enter a number: "))
if number != 0:
    if number > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")

# ============================================================
# Q21 - from q21_eligible_age_marks.py
# ============================================================
# E. Multiple Conditions - Q21. Eligible when age >= 18 and marks >= 40
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
if age >= 18 and marks >= 40:
    print("Eligible")

# ============================================================
# Q22 - from q22_special_number.py
# ============================================================
# E. Multiple Conditions - Q22. Special if number < 10 or number > 100
number = int(input("Enter a number: "))
if number < 10 or number > 100:
    print("Special")

# ============================================================
# Q23 - from q23_allowed_age_id.py
# ============================================================
# E. Multiple Conditions - Q23. Allowed when age >= 18 and has_id is True
age = int(input("Enter age: "))
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"
if age >= 18 and has_id is True:
    print("Allowed")

# ============================================================
# Q24 - from q24_both_greater_than_10.py
# ============================================================
# E. Multiple Conditions - Q24. Both numbers greater than 10
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > 10 and num2 > 10:
    print("Both are greater than 10")

# ============================================================
# Q25 - from q25_out_of_range.py
# ============================================================
# E. Multiple Conditions - Q25. Less than 0 or greater than 100
number = int(input("Enter a number: "))
if number < 0 or number > 100:
    print("Out of range")
else:
    print("In range")

# ============================================================
# Q26 - from q26_not_open.py
# ============================================================
# F. Combining Conditions - Q26. Print Open when is_closed is False using not
is_closed = False
if not is_closed:
    print("Open")

# ============================================================
# Q27 - from q27_between_10_50.py
# ============================================================
# F. Combining Conditions - Q27. Check between 10 and 50 using and
number = int(input("Enter a number: "))
if number >= 10 and number <= 50:
    print("Between 10 and 50")
else:
    print("Not between 10 and 50")

# ============================================================
# Q28 - from q28_outside_10_50.py
# ============================================================
# F. Combining Conditions - Q28. Check outside 10 to 50 using or
number = int(input("Enter a number: "))
if number < 10 or number > 50:
    print("Outside 10 to 50")
else:
    print("Inside 10 to 50")

# ============================================================
# Q29 - from q29_three_conditions.py
# ============================================================
# F. Combining Conditions - Q29. Allowed only when all three are True
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"
has_ticket = input("Do you have ticket? (yes/no): ").lower() == "yes"
if is_student and has_id and has_ticket:
    print("Allowed")
else:
    print("Not allowed")

# ============================================================
# Q30 - from q30_eligibility_checker.py
# ============================================================
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
