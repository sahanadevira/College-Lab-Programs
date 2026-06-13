def check_radius(radius):
    if radius < 0:
        #  manually trigger an error if the radius is negative
        raise RuntimeError("Area cannot be negative!")
    else:
        print(f"The radius can be used for calculation of area.The radius is {radius}.")
# Testing the program
try:
    user_input = int(input("Enter the radius: "))
    check_radius(user_input)
except RuntimeError as e:
    # This catches the error we 'raised' above OR if the user types letters
    print(f"Invalid input: {e}")

