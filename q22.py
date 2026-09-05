# 22. What is the purpose of :.2f inside an f-string?
# Answer: it formats a float to exactly 2 digits after the decimal point
# (rounds if needed). Used for prices, marks, etc.

price = 19.999
print(f"{price:.2f}")  # Output: 20.00
