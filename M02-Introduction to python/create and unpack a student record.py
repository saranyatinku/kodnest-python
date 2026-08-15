name = input()
course = input()
score = int(input())

# Create the tuple
student = (name, course, score)

# Unpack the tuple
n, c, s = student

# Display the unpacked values
print(f"Name: {n}")
print(f"Course: {c}")
print(f"Score: {s}")