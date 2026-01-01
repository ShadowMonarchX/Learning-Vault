stack = [1, 2, 3, 4, 5]

# Split the stack
s1 = [stack[0]]  # First element in s1
s2 = stack[1:][::-1]  # Remaining elements reversed in s2

print("s1 =", s1)
print("s2 =", s2)
