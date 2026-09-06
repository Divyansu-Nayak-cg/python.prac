# D. Nested Conditions - Q17. Passed -> Good / Passed, else Failed
marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 75:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")
