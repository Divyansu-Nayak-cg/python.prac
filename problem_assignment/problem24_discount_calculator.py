# 24. Discount Calculator

amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount < 500:
    discount_percent = 0
    discount_amount = amount * discount_percent / 100
    final_amount = amount - discount_amount
    print("Original amount:", amount)
    print("Discount percentage:", discount_percent)
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
elif amount <= 999:
    discount_percent = 5
    discount_amount = amount * discount_percent / 100
    final_amount = amount - discount_amount
    print("Original amount:", amount)
    print("Discount percentage:", discount_percent)
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
elif amount <= 1999:
    discount_percent = 10
    discount_amount = amount * discount_percent / 100
    final_amount = amount - discount_amount
    print("Original amount:", amount)
    print("Discount percentage:", discount_percent)
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
elif amount <= 4999:
    discount_percent = 15
    discount_amount = amount * discount_percent / 100
    final_amount = amount - discount_amount
    print("Original amount:", amount)
    print("Discount percentage:", discount_percent)
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
else:
    discount_percent = 20
    discount_amount = amount * discount_percent / 100
    final_amount = amount - discount_amount
    print("Original amount:", amount)
    print("Discount percentage:", discount_percent)
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
