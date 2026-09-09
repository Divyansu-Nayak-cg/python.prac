# 21. Triangle Type

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")
