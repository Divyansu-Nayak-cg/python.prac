# D. Nested Conditions - Q18. Positive, then greater than 100
number = int(input("Enter a number: "))
if number > 0:
    if number > 100:
        print("Positive and greater than 100")
    else:
        print("Positive but not greater than 100")
else:
    print("Not positive")
