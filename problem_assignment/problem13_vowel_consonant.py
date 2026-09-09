# 13. Vowel or Consonant

ch = input("Enter a character: ")

if (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
