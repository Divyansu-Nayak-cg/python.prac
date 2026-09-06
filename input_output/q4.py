# 4. What type of value does input() return by default?
# Answer: input() always returns a string (str) by default,
# even if the user types numbers.

value = input("Enter something: ")
print(f"Value: {value}, Type: {type(value)}")
