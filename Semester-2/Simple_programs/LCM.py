import math

a = int(input("Enter a : "))
b = int(input("Enter b : "))

c = math.gcd(a,b)

lcm = abs(a*b)//c

print("LCM is: ",lcm)
