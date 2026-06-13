print("-----TO CHECK IF THE CHIP HAS FULL ADDER APPLICATION-----")

def FullAdder(a, b, c):

    if a not in (0, 1) or b not in (0, 1) or c not in (0, 1):
        return None

    s = a ^ b
    carry = a & b
    return (s, carry)

n = int(input("Enter the number of test cases: "))

for i in range(n):
    print("-----Binary input -----")

    A = int(input("Enter the binary input_1: "))
    B = int(input("Enter the binary input_2: "))
    C = int(input("Enter the binary input_3: "))

    print("-----Binary output-----")

    result = FullAdder(A, B, C)

    if result is None:
        print("Invalid input detected. Stopping program.")
        break  # This exits the loop

    result_sum, result_carry = result
    print(f"Sum: {result_sum}, Carry: {result_carry}")
[25bec021@mepcolinux expt9]$cat fullsubtractor.py
print("-----TO CHECK IF THE CHIP HAS FULL SUBTRACTOR APPLICATION-----")

def FullSub(a, b, c):

    if a not in (0, 1) or b not in (0, 1) or c not in (0, 1):
        return None

    s = a ^ b ^ c
    carry = (~a & b) | (~( a ^ b ) & b )
    return (s, carry)

n = int(input("Enter the number of test cases: "))

for i in range(n):
    print("-----Binary input -----")

    A = int(input("Enter the binary input_1: "))
    B = int(input("Enter the binary input_2: "))
    C = int(input("Enter the binary input_3: "))

    print("-----Binary output-----")

    result = FullSub(A, B, C)

    if result is None:
        print("Invalid input detected. Stopping program.")
        break  # This exits the loop

    result_sum, result_carry = result
    print(f"Sum: {result_sum}, Carry: {result_carry}")
