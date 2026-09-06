# D. Nested Conditions - Q19. Age >= 18, then >= 60
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 60:
        print("Senior adult")
    else:
        print("Adult")
else:
    print("Minor")
