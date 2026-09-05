# 16. Why does this produce string concatenation instead of numeric addition?
# a = input()
# b = input()
# print(a + b)
# Answer: input() returns strings, so + joins (concatenates) them.
# Example: "10" + "20" -> "1020", not 30.

a = input("Enter first value: ")
b = input("Enter second value: ")
print(a + b)
