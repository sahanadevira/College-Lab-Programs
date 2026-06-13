print("Enter the coefficients of ax^2+bx+c = 0")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if (a==0):
    print("This is not a quadratic function")

discriminant = b*b - 4*a*c

if (discriminant > 0):
    root_1 = (-b + (discriminant)**0.5)/(2*a)
    root_2 = (-b - (discriminant)**0.5)/(2*a)
    print("Roots are real and distinct")
    print("The Real_root_1 is: ",root_1)
    print("The Real_root_2 is: ",root_2)
    

elif (discriminant == 0):
    root = (-b /(2*a))
    print("Roots are real and equal")
    print("The Real_root is: ",root)

elif (discriminant < 0):
    real_part = (-b //(2*a))
    imaginary_part = ((discriminant)**0.5)/(2*a)
    root_1 = real_part + imaginary_part
    root_2 = real_part - imaginary_part
    print("Roots are complex and imarginary ")
    print("The root_1 is: ", root_1)
    print("The root_2 is: ", root_2)
    
#real_and_distinct 1,-5,6
#repeated_roots 1,-4,4
#complex_roots 1,1,1

    
    
    
    



              

    
    
    



              
