str = input("Enter a word: ")

rev = ""

for i in range(len(str)-1, -1, -1):
    rev = rev + str[i]

if str == rev :
    print("Palindrome")
else:
    print("Not a palindrome")
