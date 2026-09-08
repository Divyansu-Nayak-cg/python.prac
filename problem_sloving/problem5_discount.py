
price = float(input("Enter price: "))

if price >= 1000:
    discount = price * 0.10
    final_price = price - discount
else:
    final_price = price

print(final_price)
