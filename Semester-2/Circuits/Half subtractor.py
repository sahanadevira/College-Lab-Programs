def half_subtractor(a, b):
    diff = a ^ b
    borrow = (not a) and b
    return diff, int(borrow)

print("A B Diff Borrow")

for a in range(2):
    for b in range(2):
        d, br = half_subtractor(a, b)
        print(a, b, d, br)
