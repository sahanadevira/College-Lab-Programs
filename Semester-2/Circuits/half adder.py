print("-----TO CHECK IF THE CHIP HAS HALF ADDER APPLICATION-----")

def HalfAdder(a, b):

    if a not in (0, 1) or b not in (0, 1):
        return None

    s = a ^ b
    carry = a & b
    return (s, carry)

n = int(input("Enter the number of test cases: "))

for i in range(n):
    print("-----Binary Input-----")

    A = int(input("Enter the binary input_1: "))
    B = int(input("Enter the binary input_2: "))

    print("-----Binary Ouput-----")

    result = HalfAdder(A, B)

    if result is None:
        print("Invalid input detected. Stopping program.")
        break  # This exits the loop

    result_sum, result_carry = result
    print(f"Sum: {result_sum}, Carry: {result_carry}")
