n = int(input("Enter a three digit number:"))
a = n%10
n = n//10
b = n%10
n = n//10
c = n%10
n = n//10
x = a+b+c
print("The sum of digits is:",x)
