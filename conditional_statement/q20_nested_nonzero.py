# D. Nested Conditions - Q20. Non-zero, then positive or negative
number = int(input("Enter a number: "))
if number != 0:
    if number > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")
